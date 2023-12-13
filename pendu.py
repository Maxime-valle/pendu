import pygame
import os
import random

def pendu():
    global faux
    
    pygame.init()
    pygame.mixer.init()

    #fenetre 
    win_width, win_height = 800, 600
    win = pygame.display.set_mode((win_width, win_height))

    #fond d'écran
    background = pygame.image.load(os.path.join('img87/peche13.jpg'))
    background = pygame.transform.scale(background, (win_width, win_height))

    #perso
    character = pygame.image.load(os.path.join('img87/most13.png'))  
    character = pygame.transform.scale(character, (165, 165))  
    character_x, character_y = 5, 330 

    #bande son 
    pygame.mixer.music.load("img87/legrand bleu2.mp3")
    pygame.mixer.music.set_volume(3) 
    pygame.mixer.music.play(1)

    with open("mots.txt") as fichier_txt:
        mots = fichier_txt.read().splitlines()

    font = pygame.font.Font(None, 36)  

    running = True

    def reset_game():
        global mot, mot_affiche, afficher_x, lettres_fausses, faux, mot_a_trouver
        mot = random.choice(mots)
        mot_affiche = ['_' if c != ' ' else ' ' for c in mot]
        afficher_x = False
        lettres_fausses = []  
        faux = 0  
        mot_a_trouver = mot  

    reset_game()

    while running:
        win.blit(background, (0, 0))
        win.blit(character, (character_x, character_y))

        text = font.render(' '.join(mot_affiche), True, (255, 255, 255))
        win.blit(text, (20, 20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    character_x, character_y = 5, 330
                    reset_game()
                else:
                    lettre = pygame.key.name(event.key)
                    if lettre not in mot:
                        afficher_x = True
                        lettres_fausses.append(lettre)
                        faux += 1
                        #faire avancer le personnage à chaque faute
                        character_x += 115 #  largeur du perso
                    else:
                        afficher_x = False
                        for i in range(len(mot)):
                            if mot[i] == lettre:
                                mot_affiche[i] = lettre

        texte_fausses = font.render("Lettres fausses: {}".format(" | ".join(lettres_fausses)), True, (0, 0, 0))
        win.blit(texte_fausses, (300, 90))
        # vrai ou faux 
        if faux > 3 or all(lettre in lettres_fausses for lettre in mot_a_trouver):
            texte_resultat = font.render("Dommage tu as perdu !", True, (255, 255, 255))
            win.blit(texte_resultat, (300, 130))
            texte_mot_trouve = font.render("Le mot était: {}".format(mot_a_trouver), True, (0, 0, 0))
            win.blit(texte_mot_trouve, (300, 170))
        if ''.join(mot_affiche) == mot: 
            texte_resultat = font.render("Bravo tu as gagné !", True, (255, 255, 255))
            win.blit(texte_resultat, (300, 130))
            texte_mot_trouve = font.render("Le mot était: {}".format(mot_a_trouver), True, (0, 0, 0))
            win.blit(texte_mot_trouve, (300, 170))

        texte_rejouer = font.render("Appuyez sur Entrée pour rejouer", True, (0, 0, 0))
        win.blit(texte_rejouer, (300, 210))

        pygame.display.update()

    pygame.quit()
    return True