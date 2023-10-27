import pygame
from projectile import Projectile
from monster import MonsterRight
from monster import MonsterLeft
import animation

# Créer une classe qui représente notre joueur
class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__("player")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 15
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("assets./player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500
        self.direction = "left"



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

    def update_animation(self):
        self.animate()

    def launch_projectile_right(self):
        p = Projectile(self)
        p.go_right()
        # créer une nouvelle instance de la classe projectile
        self.all_projectiles.add(p)
        # démarer l'animation du lancé
        self.start_animation()
        self.game.sound_manager.play("tir")

    def launch_projectile_left(self):
        p = Projectile(self)
        p.go_left()
        # créer une nouvelle instance de la classe projectile
        self.all_projectiles.add(p)
        self.start_animation()
        self.game.sound_manager.play("tir")


    def move_right(self):
        if not self.check_collision_with_right_monsters():
            self.rect.x += self.velocity

    def move_left(self):
        if not self.check_collision_with_left_monsters():
            self.rect.x -= self.velocity

    def check_collision_with_right_monsters(self):
        right_monsters = [monster for monster in self.game.all_monsters if isinstance(monster, MonsterRight)]
        return self.game.check_collision(self, right_monsters)

    def check_collision_with_left_monsters(self):
        left_monsters = [monster for monster in self.game.all_monsters if isinstance(monster, MonsterLeft)]
        return self.game.check_collision(self, left_monsters)