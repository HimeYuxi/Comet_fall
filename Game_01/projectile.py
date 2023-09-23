import pygame

# définir class gérant le projectile de notre joueur
class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 7
        self.player = player
        self.image = pygame.image.load("./assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origine_image = self.image
        self.angle = 0

    def rotate(self):
        # tourner le proj
        self.angle += 7
        self.image = pygame.transform.rotozoom(self.origine_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def shoot_right(self):
        self.rect.x += self.velocity
        self.rotate()

    def shoot_left(self):
        self.rect.x -= self.velocity
        self.rotate()

        # vérifier si le prof collidees with a monster
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            # infliger des dégats aux monstres
            monster.damage(self.player.attack)

        # vérifier si proj n'est plus présent sur l'écran
        if self.rect.x > 1080:
            # supprimer le projectile
            self.remove()