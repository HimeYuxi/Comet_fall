import pygame

class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f"assets/{sprite_name}.png") # = ("assets/" + sprite_name + ".png")
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0 # commencer l'anim à l'image 0
        self.images = animations.get(sprite_name)
        self.animation = False

    # def methode pour demarer l'animation
    def start_animation(self):
        self.animation = True

    # def une methode pour animer le sprite
    def animate(self):

        # verifier si l'animation est activée
        if self.animation:

            # passer à l'image suivante
            self.current_image += 1

            # vérifier si on a atteint la fin de l'animation
            if self.current_image >= len(self.images):
                self.current_image = 0
                # désactivation anim
                self.animation = False

            # modifier l'image précédente par la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)

            # flip the image if the direction is right
            if self.direction == "right":
                self.image = pygame.transform.flip(self.image, True, False)

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
    "mummy": load_animation_images("mummy"),
    "player": load_animation_images("player"),
    "alien": load_animation_images("alien"),
}
