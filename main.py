import pygame
import icon
import sys
from grille_init import GestionGrilles
import grille_init
import score
import niveau


pygame.init()

screen = pygame.display.set_mode((1270,900))

pygame.display.set_caption('PROJET FIN ANNEE')

accueil = pygame.image.load("ressources/voiture.jpg").convert()

#creation des boutons pour le menu

sprite_bouton = pygame.sprite.Group()
boutonPlay = icon.Bouton(0, 385, 350)
sprite_bouton.add(boutonPlay)
boutonEasy = icon.Bouton(1 , 385, 0)
boutonMedium = icon.Bouton(2, 385, 150)
boutonHard = icon.Bouton(3, 385, 300)

#on defini nos variables pour les boucles

running = True
running_accueil = True
running_menu = False
running_jeu = False
running_fin = False
active = False
text = ''
nom_joueur = ""
pseudo= ''
temps_de_partie = 200000
score_partie = 0
click1 = -1
click2 = -1

#On définit nos polices ainsi que leur taille
font1 = pygame.font.Font("ressources/polices/simplicity.ttf", 20)
font2 = pygame.font.Font("ressources/polices/lt_feelgood.ttf", 35)
font3 = pygame.font.Font("ressources/polices/titre_jeu.otf", 200)
font4 = pygame.font.Font("ressources/polices/titre_jeu.otf", 40)
font5 = pygame.font.Font("ressources/polices/good_people.otf", 260)

#On définit le rectangle dans lequel on va écrire notre pseudo
input_box = pygame.Rect(100, 100, 140, 32)

#On définit nos deux couleurs de cadre: une couleur quand le cadre n'est pas selectionné puis une couleur quand il est selectionné
color_inactive = pygame.Color('blue')
color_active = pygame.Color('red')

#On définit d'abord la couleur du cadre comme celle du cadre qui n'est pas selectionnée
color = color_inactive



# boucle tant que cette condition est vrai
while running:
    #mettre à jour l'ecran
    accueil = pygame.image.load("ressources/voiture.jpg").convert()
    accueil = pygame.transform.scale(accueil,(1270,900))
    screen.blit(accueil, (0,0))
    pygame.display.flip()


    while running_accueil == True:

        insererPseudo = font1.render("Inserez votre pseudo ci-dessous, puis appuyer sur 'Entrée'",3, (10, 10, 10))
        screen.blit(insererPseudo,(40,60))

        # si le joueur ferme cette fenetre
        for event in pygame.event.get():

            #ajout du tire du jeu
            nomJeu = font3.render("MATCH IT", 1, (10, 10, 10))
            screen.blit(nomJeu,(260,230))
            #crédit du jeu
            creditJeu = font1.render("Jeu crée par NELSON",4, (10, 10, 10))
            screen.blit(creditJeu,(300,660))
            #dessin du bouton play
            sprite_bouton.draw(screen)
            txt_surface = font2.render(text, True, color)
            width = max(200, txt_surface.get_width()+10)
            input_box.w = width
            screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
            pygame.draw.rect(screen, color, input_box, 2)

            # que l'evenement est fermeture de fenetre
            if event.type == pygame.QUIT:
                running_accueil = False
                running_menu = False
                running_jeu = False
                running_fin = False
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        #si on appuie sur "entrée" alors le pseudo est stocké et est affiché
                        pseudo = font2.render(text, 'maroon', (10, 10, 10))
                        screen.blit(pseudo, (250, 144))
                        nouveauJoueur = font1.render("Nouveau Joueur : ", 1, (10, 10, 10))
                        screen.blit(nouveauJoueur,(100,150))
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                    nom_joueur = text
            #evenement au clic de la souris
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = True
                else:
                    #le cadre passe en mode "selectionné"
                    active = False
                color = color_active if active else color_inactive
                posX = pygame.mouse.get_pos()[0]
                posY = pygame.mouse.get_pos()[1]
                #on verifie si le clique est sur le bouton
                if posX > 470 and posX < 720 and posY > 520 and posY < 620:
                    #on supprime le bouton play et on actualise l'ecran pour qu'il parte
                    sprite_bouton.remove(boutonPlay)
                    screen.blit(accueil, (0,0))
                    running_menu = True
                    running_accueil = False

            pygame.display.flip()

    while running_menu == True:

        #on ajoute nos 3 boutons au groupe de sprite
        sprite_bouton.add(boutonEasy)
        sprite_bouton.add(boutonMedium)
        sprite_bouton.add(boutonHard)

        #on affiche le pseudo et le nom du jeu en haut à gauche
        nomJeu = font4.render("MACHT IT", 1, (10, 10, 10))
        screen.blit(nomJeu,(30,30))
        joueurActuel = font1.render("Joueur Actuel : ", 1, (10, 10, 10))
        screen.blit(joueurActuel,(30,90))
        screen.blit(pseudo, (148, 81))

        # si le joueur ferme cette fenetre
        for event in pygame.event.get():
            #on dessine nos trois boutons
            sprite_bouton.draw(screen)
            # que l'evenement est fermeture de fenetre
            if event.type == pygame.QUIT:
                running_accueil = False
                running_menu = False
                running_jeu = False
                running_fin = False
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                posX = pygame.mouse.get_pos()[0]
                posY = pygame.mouse.get_pos()[1]
                #on verifie sur quelle bouton on clique
                #une fois clique on supprime tout les boutons et on lance le jeu
                if posX > 470 and posX < 720 and posY > 170 and posY < 270:
                    level = 0
                    nbrCase = 6
                    x = 446
                    y = 250
                    icon.supprimer(sprite_bouton, boutonEasy, boutonMedium, boutonHard)
                    running_jeu = True
                    screen.blit(accueil, (0,0))
                    #creation de notre objet grille depuis la classe GestionGrilles
                    grille = GestionGrilles(6, 6)
                    niveau.dessinNiveau(screen, 0, grille)
                    running_menu = False

                elif posX > 470 and posX < 720 and posY > 320 and posY < 420:
                    level = 1
                    nbrCase = 8
                    x = 446
                    y = 250
                    icon.supprimer(sprite_bouton, boutonEasy, boutonMedium, boutonHard)
                    running_jeu = True
                    screen.blit(accueil, (0,0))
                    #creation de notre objet grille depuis la classe GestionGrilles
                    grille = GestionGrilles(8, 8)
                    niveau.dessinNiveau(screen, 1, grille)
                    running_menu = False

                elif posX > 470 and posX < 720 and posY > 470 and posY < 570:
                    level = 2
                    nbrCase = 10
                    x = 446
                    y = 150
                    icon.supprimer(sprite_bouton, boutonEasy, boutonMedium, boutonHard)
                    running_jeu = True
                    screen.blit(accueil, (0,0))
                    #creation de notre objet grille depuis la classe GestionGrilles
                    grille = GestionGrilles(10, 10)
                    niveau.dessinNiveau(screen, 2, grille)
                    running_menu = False
            pygame.display.flip()

    #on verifie s'il n'y a pas deja des match dans notre grille de base
    grille.newtab(grille.tab_original)
    #on vide notre groupe de sprite qui contient les gem pour pouvoir actualiser la grille
    icon.vidageSprite()
    #on dessine la nouvelle grille actualise
    niveau.dessinNiveau(screen, level, grille)
    score_partie = 0

    while running_jeu == True:
        chrono = grille_init.afficher_temps(font1, screen, temps_de_partie, accueil)
        niveau.dessinGrille(screen, level)
        #on affiche le pseudo et le nom du jeu en haut à gauche pendant que le joueur joue
        nomJeu = font4.render("MATCH IT", 1, (10, 10, 10))
        screen.blit(nomJeu,(30,30))

        joueurActuel = font1.render("Joueur Actuel : ", 1, (10, 10, 10))
        screen.blit(joueurActuel,(30,90))
        screen.blit(pseudo, (148, 81))

        affichageScore = font1.render("Score : ", 1, (10, 10, 10))
        screen.blit(affichageScore, (1100,90))

        score_surface = font2.render(str(score_partie), 1, (10, 10, 10))
        screen.blit(score_surface, (1160,85))

        # si le joueur ferme cette fenetre
        for event in pygame.event.get():

            # que l'evenement est fermeture de fenetre
            if event.type == pygame.QUIT:
                running_accueil = False
                running_menu = False
                running_jeu = False
                running_fin = False
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                posX = pygame.mouse.get_pos()[0]
                posY = pygame.mouse.get_pos()[1]
                #on assigne nos click au position de la souris
                if click1 == -1:
                    #on recupere la case ou on a cliqué
                    click1 = grille.recup_case(level, posX, posY)
                elif click1 != -1:
                    click2 = grille.recup_case(level, posX, posY)
                if click1 != -1 and click2 != -1:
                    #on permutte les deux cases cliques
                    grille.permut(grille.tab_original, click1, click2)
                    #on reaactualise l'affichage en vidant le groupe de sprite
                    #et en dessinant la nouvelle grille
                    grille.newtab(grille.tab_original)
                    "score tenant compte des match lors de la creation de la grille"
                    score_partie = grille.newtab(grille.tab_original)[1]
                    print(score_partie)
                    icon.vidageSprite()
                    screen.blit(accueil, (0,0))
                    niveau.dessinNiveau(screen, level, grille)
                    #on remet nos click à leur valeur par default
                    click1 = -1
                    click2 = -1

        if chrono < 0:
            score.enregistrer_score(nom_joueur, score_partie)
            running_fin = True
            running_jeu = False


        icon.my_sprites.draw(screen)
        pygame.display.flip()

        #écran de fin
        while running_fin == True:
            screen.blit(accueil, (0,0))
            #nom du jeu
            nomJeu = font3.render("MATCH IT", 1, (10, 10, 10))
            screen.blit(nomJeu,(260,500))
            #fin du jeu

            finJeu = font5.render("Fin Du Jeu", 1, (10, 10, 10))
            screen.blit(finJeu,(90, 250))
            #nom du joueur
            joueurActuel = font1.render("Joueur Actuel : ", 1, (10, 10, 10))
            screen.blit(joueurActuel,(30,90))
            screen.blit(pseudo, (148, 81))
            #score du joueur
            scoreJoueur = font1.render("Score : ", 1, (10, 10, 10))
            screen.blit(scoreJoueur,(30,140))
            screen.blit(score_surface, (100, 135))

             # si le joueur ferme cette fenetre
            for event in pygame.event.get():

            # que l'evenement est fermeture de fenetre
                if event.type == pygame.QUIT:
                    running_accueil = False
                    running_menu = False
                    running_jeu = False
                    running_fin = False
                    sys.exit()
            pygame.display.flip()