import pygame
import random


# Créer une classe qui représente notre monstre
import game


class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load("assets./mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(1, 3)

    def damage(self, amount):
        # infliger des dégats
        self.health -= amount

        # vérifier si son nouveay nbr d'hp <= 0
        if self.health <= 0:
            # Réapparaitre comme nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
            self.health = self.max_health

            if self.game.comet_event.is_full_loaded:
                # retirer monstre
                self.game.all_monsters.remove(self)

                # appel de la méthode pour essayer de déclencher la PDC
                self.game.comet_event.attempt_fall()

    def update_health_bar(self, surface):
        # dessiner la bar de vie
        pygame.draw.rect(surface, (60, 60, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en collision avec le joueur
        else:
            # infliger des dégats
            self.game.player.damage(self.attack)