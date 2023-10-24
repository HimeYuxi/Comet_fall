
import pygame
import random

class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super(Comet, self).__init__()
        # définir l'image de comet
        self.image = pygame.image.load("assets/comet.png")
        self.rect = self.image.get_rect()
        self.velocity = random.randint(3, 5)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1000)
        self.rect.y = - random.randint(0, 1000)
        self.comet_event = comet_event
        self.attack = 20

    def remove(self):
        self.comet_event.all_comets.remove(self)

        # vérifier si le nombrree de comètes est de 0
        if len(self.comet_event.all_comets) == 0:
            # remettre la barre à 0
            self.comet_event.reset_percent()
            # réapparition des streums
            self.comet_event.fall_mode = False
            self.comet_event.reset_max_comets()



    def fall(self):
        self.rect.y += self.velocity

        # ne tombe pas sur le sol
        if self.rect.y >= 540:
            # retirer la boule de feu
            self.remove()

            # s'il n'y a plus dee boules de feu sur le jeu
            if len(self.comet_event.all_comets) == 0:
                # remettre la jauge à 0
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        if self.comet_event.game.check_collision(
            self, self.comet_event.game.all_players
        ):
            self.remove()
            self.comet_event.game.player.damage(self.attack)
