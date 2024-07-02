import pygame
import icon


def dessinerColonne(marge, pntDepart, pntArrivee, longueur):
    """fonction permettant de dessiner un trait entre le point de depart de notre colonne
    et le point d'arrive de la colonne en tenant compte de la marge pour pouvoir centrer la grille"""
    colonne = [((marge + i * 50, pntDepart), (marge + i * 50, pntArrivee)) for i in range(1, longueur)]
    return colonne


def dessinerLigne(marge, pntDepart, pntArrivee, longueur):
    """fonction permettant de dessiner un trait entre le point de depart de notre colonne
     et le point d'arrive de la colonne en tenant compte de la marge pour pouvoir centrer la grille"""
    ligne = [((pntDepart, (marge + 50 * i)), (pntArrivee, (marge + i * 50))) for i in range(1, longueur)]
    return ligne


def dessinNiveau(screen, niveau, grille):
    # taille de la grille suivant le niveau

    if niveau == 0:
        # taille 6*6
        ligne = dessinerLigne(200, 450, 750, 8)
        colonne = dessinerColonne(400, 250, 550, 8)
        icon.remplissageGem(446, 250, 6, grille)

    elif niveau == 1:
        # taille 8*8
        ligne = dessinerLigne(200, 450, 850, 10)
        colonne = dessinerColonne(400, 250, 650, 10)
        icon.remplissageGem(446, 250, 8, grille)

    elif niveau == 2:
        # taille 10*10
        ligne = dessinerLigne(100, 450, 950, 12)
        colonne = dessinerColonne(400, 150, 650, 12)
        icon.remplissageGem(446, 150, 10, grille)

    for i in ligne:
        pygame.draw.line(screen, (255, 255, 255), i[0], i[1], 1)

    for i in colonne:
        pygame.draw.line(screen, (255, 255, 255), i[0], i[1], 1)


def dessinGrille(screen, niveau):
    if niveau == 0:
        # taille 6*6
        ligne = dessinerLigne(200, 450, 750, 8)
        colonne = dessinerColonne(400, 250, 550, 8)

    elif niveau == 1:
        # taille 8*8
        ligne = dessinerLigne(200, 450, 850, 10)
        colonne = dessinerColonne(400, 250, 650, 10)

    elif niveau == 2:
        # taille 10*10
        ligne = dessinerLigne(100, 450, 950, 12)
        colonne = dessinerColonne(400, 150, 650, 12)

    for i in ligne:
        pygame.draw.line(screen, (255, 255, 255), i[0], i[1], 1)

    for i in colonne:
        pygame.draw.line(screen, (255, 255, 255), i[0], i[1], 1)

