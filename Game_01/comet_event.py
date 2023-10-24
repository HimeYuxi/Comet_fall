import pygame
from comet import Comet


# créer une classe pour gérer cet event
class CometFallEvent:

    # lors du chargement -> créer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 10
        self.game = game
        self.fall_mode = False
        self.max_comets_reached = False

        # def grp de sprites pour stocker nos comètes
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def reset_max_comets(self):
        self.max_comets_reached = False

    def comet_fall(self, max_comets=10):
        # Check if the maximum number of comets has been reached
        if not self.max_comets_reached:
            # Boucle les valeurs entre 1 et 10
            for i in range(min(max_comets, 10 - len(self.all_comets))):
                # Apparaitre boule de feu
                comet = Comet(self)
                self.all_comets.add(comet)
                # Check if the maximum number of comets has been reached after adding a new comet
                if len(self.all_comets) >= max_comets:
                    self.max_comets_reached = True

    def attempt_fall(self):
        # La jauge d'event est chargée
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            print("Pluie de comètes !")
            self.comet_fall()
            self.fall_mode = True

    def update_bar(self, surface):

        # ajouter du pourcentage à la barre
        self.add_percent()

        # barre noire (en arrière plan)
        pygame.draw.rect(surface, (0, 0, 0),[
            0, # abcisses
            surface.get_height() - 20, # ordonnées
            surface.get_width(), # longueur de ma fenêtre
            10 # épaisseur de la barre
        ])

        # barre rouge (jauge d'event)
        pygame.draw.rect(surface, (187, 11, 11),[
            0, # abcisses
            surface.get_height() - 20, # ordonnées
            (surface.get_width() / 100) * self.percent, # longueur de ma fenêtre
            10 # épaisseur de la barre
        ])