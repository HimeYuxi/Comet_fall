import random

import pygame.sprite

from player import Player
from monster import MonsterRight, MonsterLeft, MummyRight, MummyLeft, AlienRight, AlienLeft
from comet_event import CometFallEvent
from sounds import SoundManager


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
        self.monster_spawn_allowed = True
        self.sound_manager = SoundManager()
        self.font = pygame.font.SysFont("monospace", 40, bold=True)
        self.score = 0
        self.pressed = {}

    def start(self):
        self.is_playing = True

    def add_score(self, points=1):
        self.score += points

    def game_over(self):
        # remettre le jeu à neuf, retirer les monstres, remettre le joueur à 100 de vie, jeu en attente
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.all_projectiles = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 0
        self.sound_manager.play("game_over")


    def update(self, screen):
        # afficher le score à l'écran
        score_text = self.font.render(f"Score : {self.score}", 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))

        # appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)
        self.player.update_animation()

        # actualiser la barre d'event du jeu
        self.comet_event.update_bar(screen)

        if self.comet_event.attempt_fall():
            self.monster_spawn_allowed = False
        else:
            self.monster_spawn_allowed = True

        if self.monster_spawn_allowed and not self.comet_event.is_full_loaded():
            self.spawn_monster()


        # récup les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # les streums
        for monster in self.all_monsters:
            if isinstance(monster, MonsterRight):
                monster.forward_left()
            elif isinstance(monster, MonsterLeft):
                monster.forward_right()
            monster.update_health_bar(screen)
            monster.update_animation()

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

    def spawn_monster(self, max_monsters=4):
        if len(self.all_monsters) < max_monsters:

            monster_types = [
                (MummyRight, 0.9),
                (MummyLeft, 0.9),
                (AlienRight, 0.1),
                (AlienLeft, 0.1)
            ]

            chosen_monster_type, probability = random.choices(monster_types)[0]

            if random.random() < probability:  # Check if the random number is less than the probability
                monster = chosen_monster_type(self)
                self.all_monsters.add(monster)
