from guizero import Drawing
from PIL import Image, ImageTk
from Box2D import *
from .thing import *
from math import pi,sqrt
from time import time

class ebImage(ebThing):
    def __init__(self, box, x, y, width, height, **kwargs):
        world  = box.world
        canvas = box.canvas

        # mémorisation de la box
        self.box   = box

        # paramètres
        self._type      = kwargs.pop('type', 'dynamic')
        self._file      = kwargs.pop('image', None)

        # paramètres body
        angle           = kwargs.pop('angle', 0)
        fixedRot        = kwargs.pop('fixedRotation', False)
        self._noRot     = kwargs.pop('noRotation', False)
        bullet          = kwargs.pop('bullet', False)

        # paramètres fixture
        dens            = kwargs.pop('density', 1)
        fric            = kwargs.pop('friction', 0)
        rest            = kwargs.pop('restitution', 0)
        imShape         = kwargs.pop('imShape', 'rectangle')

        # body box2d
        if self._type=='static':
            constructor = world.CreateStaticBody
        elif self._type=='kinematic':
            constructor = world.CreateKinematicBody
        else:
            constructor = world.CreateDynamicBody
        body = constructor(
            position = (x/box.scale, box._height-y/box.scale),
            angle=angle,
            fixedRotation=fixedRot,
            bullet=bullet,
        )

        # on enregistre le lien avec le body
        self.body     = body
        body.userData = self

        # fixture et shape box2d
        if imShape=='rectangle':
            # shape rectangle par défaut
            body.CreatePolygonFixture(
                box=(width/box.scale/2, height/box.scale/2, (0,0), 0),
                density=dens,
                friction=fric,
                restitution=rest,
            )
        elif imShape=='circle':
            # shape circle
            r = max(width/box.scale/2, height/box.scale/2)
            body.CreateCircleFixture(
                radius=r,
                density=dens,
                friction=fric,
                restitution=rest,
            )

        # lecture des dimensions de l'image et calcul du ratio
        if self._file:
            with Image.open(self._file) as img:
                w, h        = img.size
                ratio       = (width/w, height/h)
                self._ratio = ratio

        # item canvas
        self.item   = None
        if self._file and not self._noRot:
            # l'image est censée tourner
            # ouverture de l'image
            with Image.open(self._file) as img:
                # on étend l'image avec des pixels transparents
                # pour pouvoir la tourner sans perdre de pixels
                side  = round(sqrt(w**2+h**2))
                new = Image.new('RGBA', (side, side), (0, 0, 0, 0))
                new.paste(  img,
                            (round((side-w)/2), round((side-h)/2)),
                            img.convert('RGBA')
                )
            # nouvelles dimensions
            img  = new
            w, h = img.size
            # stockage de l'image
            self._img   = []
            # top départ
            t0          = time()
            # on tourne l'image par pas de 1°
            for angle in range(360):
                # identifiant de l'image
                imageId = self._file + '-' + str(width) + '-' + str(height) + '-' + str(angle)
                # si l'image tournée a déjà été calculée on la retrouve
                if imageId in box._images.keys():
                    self._img.append(box._images[imageId])
                # sinon on la calcule
                else:
                    # rotation
                    new = img.rotate(angle)
                    # redimensionnement
                    # c'est plus long de le faire ici, mais le résultat est meilleur...
                    new = new.resize(
                            (round(w*ratio[0]),round(h*ratio[1])),
                            # Image.NEAREST,
                            # Image.BICUBIC,
                            Image.LANCZOS,
                    )
                    # stockage
                    pimg = ImageTk.PhotoImage(new)
                    box._images[imageId] = pimg
                    self._img.append(pimg)
            # temps écoulé
            elapsed = round(100*(time()-t0))/100
            # affichage du temps écoulé
            if elapsed:
                print(  '{} : {}s'.format(self._file,
                        str(round(100*(time()-t0))/100))
                    )
            # placement de l'image dans le Canvas
            pos         = body.position
            angle       = round(body.transform.angle*180/pi)
            self.item   = canvas.create_image(
                                pos[0]*box.scale,
                                (box._height - pos[1])*box.scale,
                                image=self._img[angle],
                                **kwargs,
                    )
        elif self._file and self._noRot:
            # l'image est bloquée en rotation
            self.setImage(self._file, **kwargs)

    @property
    def angle(self):
        # angle en radian
        return self.body.transform.angle

    @angle.setter
    def angle(self, value):
        self.body.angle = value
        if self._noRot:
            # image dont l'affichage ne suit pas
            # la rotation de l'objet physique
            self.setImage(self._file)
        else:
            # image dont l'affichage suit
            # la rotation de l'objet physique
            canvas = self.box.canvas
            canvas.itemconfigure(self.item, image=self._img[angle])

    def setImage(self, file, **kwargs):
        self._file = file
        # recharge l'image si elle est bloquée en rotation uniquement
        if self._noRot:
            self._img   = []
            # on récupère d'abord ce dont on a besoin
            ratio  = self._ratio
            body   = self.body
            box    = self.box
            canvas = box.canvas
            angle  = round(body.transform.angle*180/pi)
            # identifiant de l'image
            imageId = file + '-' + str(angle)
            # si l'image tournée a déjà été calculée on la retrouve
            if imageId in box._images.keys():
                self._img.append(box._images[imageId])
            # sinon on la calcule
            else:
                # agrandissement de l'image
                with Image.open(file) as img:
                    w, h   = img.size
                    side   = round(sqrt(w**2+h**2))
                    # on étend l'image avec des pixels transparents
                    # pour pouvoir la tourner sans perdre de pixels
                    new = Image.new('RGBA', (side, side), (0, 0, 0, 0))
                    new.paste(  img,
                                (round((side-w)/2), round((side-h)/2)),
                                img.convert('RGBA')
                    )
                # nouvelles dimensions
                w, h   = new.size
                # rotation de l'image
                new    = new.rotate(angle)
                # redimensionnement
                new    = new.resize(
                                (round(w*ratio[0]),round(h*ratio[1])),
                                # Image.NEAREST,
                                # Image.BICUBIC,
                                Image.LANCZOS,
                        )
                # stockage de l'image
                pimg = ImageTk.PhotoImage(new)
                box._images[imageId] = pimg
                self._img.append(pimg)
            # destruction de l'ancien item du Canvas
            canvas.delete(self.item)
            # placement de l'image dans le Canvas
            pos    = body.position
            item   = canvas.create_image(
                            pos[0]*box.scale,
                            (box._height - pos[1])*box.scale,
                            image=self._img[0],
                            **kwargs,
                        )
            # on mémorise le nouvel item
            self.item     = item

    def update_item(self):
        box    = self.box
        body   = self.body
        canvas = box.canvas
        pos    = body.position
        shape  = body.fixtures[0].shape
        angle  = round(body.transform.angle*180/pi)
        # rotation de l'image si nécessaire
        if not self._noRot:
            canvas.itemconfigure(self.item, image=self._img[angle])
        # déplacement de l'image
        canvas.coords(self.item, box.toCanvasCoords(*pos))
