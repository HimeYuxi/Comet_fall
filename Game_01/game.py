import pygame.sprite

from player import Player
from monster import Monster
from comet_event import CometFallEvent

# créer une seconde classe qui va représenter notre jeu
class Game:

    def __init__(self):
        # def si le jeu à commencé ou non
        self.is_playing = False
        # generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # générer l'event
        self.comet_event = CometFallEvent(self)
        # groupe de monstres
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()
        self.spawn_monster()


    def game_over(self):
        # remettre le jeu à neuf, retirer les monstres, remettre le joueur à 100 de vie, jeu en attente
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.all_projectiles = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False

    def update(self, screen):
        # appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # actualiser la barre d'event du jeu
        self.comet_event.update_bar(screen)

        # récup les projectiles du joueur
        for projectile in self.player.all_projectiles:
            if self.pressed.get(pygame.K_RIGHT):
                projectile.shoot_right()

            if self.pressed.get(pygame.K_LEFT):
                projectile.shoot_left()

        # les streums
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # les comètes
        for comet in self.comet_event.all_comets:
            comet.fall()

        # appliquer l'ensemble des images de mon grp de projectiles
        self.player.all_projectiles.draw(screen)

        # pareil avec les streumons
        self.all_monsters.draw(screen)

        # same pour les comètes
        self.comet_event.all_comets.draw(screen)

        # vérifier si le joueur souhaite aller à gauche ou droite
        if self.pressed.get(pygame.K_d) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_q) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)

