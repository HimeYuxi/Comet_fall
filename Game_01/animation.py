import pygame

class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f"assets/{sprite_name}.png") # = ("assets/" + sprite_name + ".png")
        self.current_image = 0 # commencer l'anim à l'image 0
        self.images = animations.get(sprite_name)

    # def une methode pour animer le sprite
    def animate(self):

        # passer à l'image suivante
        self.current_image += 1

        # vérifier si on a atteint la fin de l'animation
        if self.current_image >= len(self.images):
            self.current_image = 0

        # modifier l'image précédente par la suivante
        self.image = self.images[self.current_image]

# def fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    # charger les 24 images de ce sprite dans le dossier correspondant
    images = []
    # récup le chemin du dossier pour ce sprite
    path = f"assets/{sprite_name}/{sprite_name}"

    #boucler sur chaque image dans ce dossier
    for num in range(1, 24):
        image_path = path + str(num) + ".png"
        images.append(pygame.image.load(image_path))

    # renvoyer le contenu de la liste d'image
    return images

# definir dico qui va contenir les images chargées de chaque sprite
# mummy -> [...mummy1.png, ...mummy2.png,...]
animations = {
    "mummy": load_animation_images("mummy")
}
