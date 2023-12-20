import pygame
import os
import random
import subprocess
from pendu2 import difficile
from pendu import pendu

def niveau_pendu():
    pygame.init()
    pygame.mixer.init()

    #fenetre 
    win_width, win_height = 800, 600
    win = pygame.display.set_mode((win_width, win_height))

    #fond d'écran
    background = pygame.image.load(os.path.join('img87/Menu14.jpg'))
    background = pygame.transform.scale(background, (win_width, win_height))

    # Bande son
    pygame.mixer.music.load("img87/music menu.mp3")
    pygame.mixer.music.set_volume(3)
    pygame.mixer.music.play(1)

    # Dessiner le fond d'écran sur la fenêtre
    win.blit(background, (0, 0))

    # Ajout de boutons
    button_width, button_height = 100, 50  
    button_color = (50, 50, 50)
    button1_pos = (win_width/2 - button_width - 10, win_height/2 - button_height/2)  #  bouton 1
    button2_pos = (win_width/2 + 10, win_height/2 - button_height/2)  # bouton 2
    pygame.draw.rect(win, button_color, pygame.Rect(*button1_pos, button_width, button_height))  # bouton 1
    pygame.draw.rect(win, button_color, pygame.Rect(*button2_pos, button_width, button_height))  # bouton 2

    # Ajout de texte sur les boutons
    font = pygame.font.Font(None, 36)  # Créer une police
    text1 = font.render('Difficile', True, (255, 255, 255))  # Créer le texte pour le bouton 1
    text2 = font.render('Facile', True, (255, 255, 255))  # Créer le texte pour le bouton 2
    win.blit(text1, (button1_pos[0] + (button_width - text1.get_width()) // 2, button1_pos[1] + (button_height - text1.get_height()) // 2))  # Dessiner le texte sur le bouton 1
    win.blit(text2, (button2_pos[0] + (button_width - text2.get_width()) // 2, button2_pos[1] + (button_height - text2.get_height()) // 2))  # Dessiner le texte sur le bouton 2

    pygame.display.update()

    # Boucle principale
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()  
            
                # Vérifier si l'un des boutons a été cliquer
                if button1_pos[0] <= mouse_pos[0] <= button1_pos[0] + button_width and button1_pos[1] <= mouse_pos[1] <= button1_pos[1] + button_height:
                    difficile()
                    subprocess.run(["python", "pendu.py"], check=True)  # Ouvrir le fichier pendu.py
                elif button2_pos[0] <= mouse_pos[0] <= button2_pos[0] + button_width and button2_pos[1] <= mouse_pos[1] <= button2_pos[1] + button_height:
                    pendu()
    pygame.quit()