
from random import randrange,randint
import pygame

NORD, EST, SUD, OUEST = 0, 1, 2, 3


def create(lin, col, init):
    """ crée une grille avec pour nombre de ligne 'lin' et pour
    nombre de colonne 'col' avec pour nombre initial 'init'"""
    return [[init] * col for _ in range(lin)]


def create_alea(lin, col, mini=10, maxi=100):
    """Retourne une grille  de ``lin`` lignes de ``col``colonnes et  valeurs dans [``mini``, ``maxi``[."""
    return [[randrange(mini, maxi) for _ in range(col)] for _ in range(lin)]

def shape(tab):
    """ extrait la forme de ``tab``."""
    nb_lig = len(tab)
    nb_col = len(tab[0]) if nb_lig else 0
    return nb_lig, nb_col


def line_str(tab, i):
    """affiche proprement la ligne ``i`` de ``tab``."""
    return '|\t' + '\t'.join(str(val) for val in tab[i]) + '\t|'


def to_str(tab):
    """affiche proprement ``tab``."""
    res = ''
    for i in range(len(tab)):
        res += '\n' + line_str(tab, i)
    return res


def line(tab, i):
    """extrait la ième ligne de ``tab``."""
    return tab[i]
def column(tab, j):
    """extrait la ième colonne de ``tab``."""
    return [line[j] for line in tab]


def add(tab):
    """fait la somme de tous les élements de ``tab``"""
    return sum(sum(line) for line in tab)


def case_to_lc(tab, num_case):
    """converti un numéro de case ``num_case`` de ``tab`` vers les coordonnées (ligne, colonne)  correspondants."""
    _, nb_col = shape(tab)
    return num_case // nb_col, num_case % nb_col


def lc_to_case(tab, num_lig, num_col):
    """converti les coordonnées (``num_lig``, ``num_col``) de ``tab`` vers le numéro de case correspondant."""
    return num_lig * shape(tab)[1] + num_col

def get_case(tab, num_case):
    """ extrait la valeur de ``tab`` en ``num_case``."""
    lig, col = case_to_lc(tab, num_case)
    return tab[lig][col]



def lig_col_next(tab, lig, col, direction=NORD, tore=False):
    """calcule la paire (ligne, colonne) suivant (``lig``, ``col``) dans ``tab`` dans la direction ``direction``
        si ``tore`` est True, le dépassement des limites est géré en considérant la grilles comme un tore
        si ``tore`` est False, le dépassement des limites produit -1
    """
    nb_lig, nb_col = shape(tab)
    new_lig, new_col = lig, col
    if direction == NORD:
        if not tore and lig == 0:
            return -1
        new_lig, new_col = (lig - 1) % nb_lig, col
    if direction == EST:
        if not tore and col == nb_col - 1:
            return -1
        new_lig, new_col = lig, (col + 1) % nb_col
    if direction == SUD:
        if not tore and lig == nb_lig - 1:
            return -1
        new_lig, new_col = (lig + 1) % nb_lig, col
    if direction == OUEST:
        if not tore and col == 0:
            return -1
        new_lig, new_col = lig, (col - 1) % nb_col
    return new_lig, new_col

# remplacer 3 nombres identiques successives ou plus en lignes et en colonnes par des 0

class GestionGrilles:
    "classe qui prend en paramètre les dimensions de la grille souhaite"

    def __init__(self, n, m):
        self.tab_original =create_alea(n, m, 1, 5)
        self.score_lig = 0
        self.score_col = 0
        self.score = 0

    def remplissage(self, tab):
        "on remplit aleatoirement la grille de 1,2,3,4 qui correspondent aux identifiants des gems"
        for l in range(4):
            for i in range(len(tab) - 1, 0, -1):
                for j in range(len(tab[0]) - 1, -1, -1):
                    if tab[i][j] == 0:
                        for k in range(i, 0, -1):
                            tab[k][j] = tab[k - 1][j]
                            tab[k - 1][j] = 0
            print(to_str(tab))
        for i in range(len(tab)):
            for j in range(len(tab[0])):
                if tab[i][j] == 0:
                    tab[i][j] = randint(1, 4)
        return tab

    def eliminerLignes(self, tab):
        "fonction qui permet d'eliminer l'endroit d'en la ligne ou il y a 3 meme chiffres a la suite"
        newtab_index = create(len(tab), len(tab[0]), 0)
        for i in range(len(tab)):
            soustab_lig =line(tab, i)  # on crée une variable devant compté le nombre de ligne  identique
            for j in range(0, len(soustab_lig) - 2):
                if (soustab_lig[j] == soustab_lig[j + 1] == soustab_lig[j + 2]):
                    newtab_index[i][j] = 1
                    newtab_index[i][j + 1] = 1
                    newtab_index[i][j + 2] = 1
                    if soustab_lig[j] == 1:
                        self.score_lig += 00 # score pour
                    if soustab_lig[j] == 2:
                        self.score_lig += 00
                    if soustab_lig[j] == 3:
                        self.score_lig += 10
                    if soustab_lig[j] == 4:
                        self.score_lig += 20
                    if soustab_lig[j] == 5:
                        self.score_lig += 50
                    if soustab_lig[j] == 6:
                        self.score_lig += 100
        for i in range(len(tab)):
            for j in range(len(tab[0])):
                if newtab_index[i][j] == 1:
                    tab[i][j] = 0
        return tab, self.score_lig

    def eliminerColonnes(self, tab):
        "fonction qui permet d'eliminer l'endroit d'en la colonne ou il y a 3 meme chiffre a la suite"
        newtab_index =create(len(tab), len(tab[0]), 0)
        for i in range(len(tab[0])):
            soustab_col =column(tab, i)
            for j in range(0, len(soustab_col) - 2):
                if (soustab_col[j] == soustab_col[j + 1] == soustab_col[j + 2]):
                    newtab_index[i][j] = 1
                    newtab_index[i][j + 1] = 1
                    newtab_index[i][j + 2] = 1
                    if soustab_col[j] == 1:
                        self.score_col += 00
                    if soustab_col[j] == 2:
                        self.score_col += 00
                    if soustab_col[j] == 3:
                        self.score_col += 10
                    if soustab_col[j] == 4:
                        self.score_col += 20
                    if soustab_col[j] == 5:
                        self.score_col += 50
                    if soustab_col[j] == 6:
                        self.score_col += 100

        for i in range(len(tab)):
            for j in range(len(tab[0])):
                if newtab_index[i][j] == 1:
                    tab[j][i] = 0
        return tab, self.score_col

    def eliminerLignesColonnes(self, tab):
        "fonction qui elimine 3 meme chiffre qui sont a la suite"
        ntab1 = self.eliminerLignes(tab)[0]
        ntab2 = self.eliminerColonnes(tab)[0]
        self.score = self.eliminerLignes(tab)[1] + self.eliminerColonnes(tab)[1]
        for l in range(len(tab)):
            for k in range(len(tab[l])):
                if ntab1[l][k] == 0 or ntab2[l][k] == 0:
                    tab[l][k] = 0
        return tab, self.score

    def count_zero(self, tab):
        for i in range(len(tab)):
            for j in range(len(tab[0])):
                if tab[i][j] == 0:
                    return True
        return False

    def newtab(self, tab):
        "fonction qui renvoie une nouvelle grille où on a enlever les elements identiques"
        grille = self.eliminerLignesColonnes(tab)[0]
        self.score = self.eliminerLignesColonnes(tab)[1]
        self.remplissage(grille)
        self.eliminerLignesColonnes(grille)
        while self.count_zero(grille):
            self.remplissage(grille)
            self.eliminerLignesColonnes(grille)[0]
        print(to_str(grille))
        return grille, self.score

    def recup_case(self, level, x, y):
        "fonction qui permet de recuperer les coordonnes de la case dans la quelle on vient de cliquer"
        if level == 2:  # on specifie le niveau pour pouvoir avoir les coordonnées exactes
            return (((y - 150) // 50), (x - 450) // 50)
        else:
            return (((y - 250) // 50), (x - 450) // 50)

    def permut(self, tab, click1, click2):
        "fonction qui permet d'echanger des cases si elles sont a cotes et remplis avec les cases qui sont autour"
        if click1 != click2:
            if (click1[0] == click2[0] and (click1[1] == click2[1] + 1 or click1[1] == click2[1] - 1)) or (
                    click1[1] == click2[1] and (click1[0] == click2[0] + 1 or click1[0] == click2[0] - 1)):
                a = tab[click1[0]][click1[1]]
                tab[click1[0]][click1[1]] = tab[click2[0]][click2[1]]
                tab[click2[0]][click2[1]] = a
                print(to_str(tab))
        return tab


def afficher_temps(font, screen, temps_de_partie, accueil):
    """fonction qui prend en paramètre le style d'ecriture, l'ecran, le temps que doit durer la partie
    et le fond d'ecran.
    Cette fonction permet d'afficher et de calculer le temps restant de la partie """
    screen.blit(accueil, (0, 0))
    temps = (temps_de_partie - pygame.time.get_ticks()) // 1000
    affichageTemps = font.render("Temps : ", 1, (10, 10, 10))
    screen.blit(affichageTemps, (1091, 120))

    temps_surface = font.render(str(temps), 1, (10, 10, 10))
    screen.blit(temps_surface, (1160, 120))

    return temps



