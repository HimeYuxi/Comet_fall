import pygame
import math
import time
from game import Game
pygame.init()
pygame.key.set_repeat(150, 150)

# Générer la fenetre de jeu
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1200, 720))

background = pygame.image.load("assets/bg.jpg")

# importer notre banière
banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 3.5)

# import charger un bouton  pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# charger notre jeu
game = Game()
clock = pygame.time.Clock()
FPS = 60
time = time
running = True

# boucle tant que cette condition est vraie
while running:

    clock.tick(FPS)

    # appliquer arrière plan du jeu
    screen.blit(background, (-100, -200))

    # vérifier si le jeu à commencé ou pas
    if game.is_playing:
        # déclencher les instructions de la partie
        game.update(screen)
    # vérifier si le jeu n'a pas encore commencé
    else:
        # ajouter mon écran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)


    # mettre à jour l'écran
    pygame.display.flip()

    # si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")

        # détécter si un joueur lâche une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # détécter si les touches flèches sont enclenchées pour lancer un projectile
            if event.key == pygame.K_RIGHT:
                game.player.launch_projectile_right()

            if event.key == pygame.K_LEFT:
                game.player.launch_projectile_left()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game.is_playing == False:
                # vérificationpour savoir si la souris est en collision avec le bouton play
                if play_button_rect.collidepoint(event.pos):
                    # mettre le jeu en mode "lancé"
                    game.start()
                    game.sound_manager.play("click")

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if game.is_playing == False:
                # mettre le jeu en mode "lancé"
                game.start()
                game.sound_manager.play("click")
