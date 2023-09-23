import pygame
from projectile import Projectile

# Créer une classe qui représente notre joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 15
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("assets./player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):
        if self.health - amount >= 0:
            self.health -= amount
            print(self.health)
            # si le joueur n'a plus de vie
        else:
            self.game.game_over()

    def update_health_bar(self, surface):
        # dessiner la bar de vie
        pygame.draw.rect(surface, (60, 60, 60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 7])

    def launch_projectile(self):
        # créer une nouvelle instance de la classe projectile
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
