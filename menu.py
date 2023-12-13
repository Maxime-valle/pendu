import pygame
import os
import cv2
import pygame_gui
from pendu import pendu

pygame.init()

# Fenêtre
largeur_fenetre, hauteur_fenetre = 800, 800
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

# pygame_gui
gestionnaire = pygame_gui.UIManager((largeur_fenetre, hauteur_fenetre))

# Bouton
bouton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((largeur_fenetre // 2 - 80, hauteur_fenetre // 2 - 205), (150, 50)),
                                      text='Aller à pendu',
                                      manager=gestionnaire)

# fond ecran opencv
chemin_video = os.path.join('img87', 'fond ecran 22.mp4')
cap = cv2.VideoCapture(chemin_video)

# Variables 
en_cours = True
aller_a_pendu = False

# Bande son
pygame.mixer.music.load("img87/music menu.mp3")
pygame.mixer.music.set_volume(3)
pygame.mixer.music.play(1)

while en_cours:
    delta_temps = pygame.time.Clock().tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

        gestionnaire.process_events(event)

        # Le bouton, définir aller_a_pendu sur True
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == bouton:
                    aller_a_pendu = True
                    en_cours = False  # Sortir de la boucle while

    gestionnaire.update(delta_temps)

    if not aller_a_pendu:
        # Frame de la vidéo avec OpenCV
        ret, frame = cap.read()
        if not ret:
            # Si la vidéo est terminée, revenir au début
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        #  pivoter l'image
        frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)

        # Redimensionner l'image à la taille de la fenêtre Pygame
        frame = cv2.resize(frame, (largeur_fenetre, hauteur_fenetre))

        # Convertir l'image OpenCV en surface Pygame
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = pygame.surfarray.make_surface(frame)
        fenetre.blit(frame, (0, 0))

        gestionnaire.draw_ui(fenetre)
        pygame.display.update()

if aller_a_pendu:
    pendu()

#  les ressources
cap.release()
cv2.destroyAllWindows()