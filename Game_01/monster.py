import pygame
import random
import animation

# Créer une classe qui représente notre monstre
import game


class MonsterRight(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.y = 540 - offset
        self.rect.x = 1200 + random.randint(0, 300)
        self.velocity = random.randint(1, 3)
        self.direction = "left"

        '''
        if random.choice([True, False]):
            self.flipped_image = self.image
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
        else:
            self.image = self.flipped_image
            self.rect.x = -random.randint(0, 300)
            self.velocity = -random.randint(1, 3)
        '''

    def damage(self, amount):
        # infliger des dégats
        self.health -= amount

        # vérifier si son nouveay nbr d'hp <= 0
        if self.health <= 0:

            if self.game.comet_event.is_full_loaded:
                # retirer monstre
                self.game.all_monsters.remove(self)

                # appel de la méthode pour essayer de déclencher la PDC
                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate()


    def update_health_bar(self, surface):
        # dessiner la bar de vie
        pygame.draw.rect(surface, (60, 60, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def forward_left(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
            self.start_animation()
        # si le monstre est en collision avec le joueur
        else:
            # infliger des dégats
            self.game.player.damage(self.attack)


################################################################


class MonsterLeft(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.y = 540 - offset
        self.rect.x = -random.randint(50, 350)
        self.velocity = random.randint(1, 3)
        self.direction = "right"

        '''
        if random.choice([True, False]):
            self.flipped_image = self.image
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
        else:
            self.image = self.flipped_image
            self.rect.x = -random.randint(0, 300)
            self.velocity = -random.randint(1, 3)
        '''


    def damage(self, amount):
        # infliger des dégats
        self.health -= amount

        # vérifier si son nouveay nbr d'hp <= 0
        if self.health <= 0:

            if self.game.comet_event.is_full_loaded:
                # retirer monstre
                self.game.all_monsters.remove(self)

                # appel de la méthode pour essayer de déclencher la PDC
                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate()


    def update_health_bar(self, surface):
        # dessiner la bar de vie
        pygame.draw.rect(surface, (60, 60, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def forward_right(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x += self.velocity
            self.start_animation()
        # si le monstre est en collision avec le joueur
        else:
            # infliger des dégats
            self.game.player.damage(self.attack)


################################################################################

# définir une classe pour la momie

class MummyRight(MonsterRight):

    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))

class MummyLeft(MonsterLeft):

    def __init__(self, game):
        super().__init__(game, "mummy",(130,130))

# clase pour l'alien

class AlienRight(MonsterRight):

    def __init__(self, game):
        super().__init__(game, "alien", (250, 250), 100)
        self.health = 200
        self.max_health = 200
        self.velocity = 1
        self.attack = 0.8

class AlienLeft(MonsterLeft):

    def __init__(self, game):
        super().__init__(game, "alien", (250, 250), 100)
        self.health = 200
        self.max_health = 200
        self.velocity = 1
        self.attack = 0.8
