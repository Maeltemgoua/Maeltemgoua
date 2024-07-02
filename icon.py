import pygame

# listes contenant les chemin d'accès des images dans notre répertoire
liste = ["ressources/gemmes/gemme_verte.png", "ressources/gemmes/gemme_rouge.png", "ressources/gemmes/gemme_jaune.png",
         "ressources/gemmes/gemme_rose.png"]
my_sprites = pygame.sprite.Group()


class Gem(pygame.sprite.Sprite):
    "classe pour initilaiser mes gems qui prend en parametre les coordonnees et le chemin"

    def __init__(self, x, y, id):
        self.id = id
        pygame.sprite.Sprite.__init__(self)
        # on recupere les chemins pour charger les images
        self.image = pygame.image.load(liste[id - 1])
        # redimensionne les images pour eviter de perdre en qualites
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)


def remplissageGem(x, y, nbrCase, grille):
    """ fonction qui prend en paramètre des coordonnées x et y qui correspondent
    aux cases de la grille ainsi que le nombre de case.
    Les cases sont remplis aléatoirement avec les images de nos gemmes."""
    for i in range(nbrCase):
        for j in range(nbrCase):
            my_sprites.add(Gem(x, y, grille.tab_original[i][j]))
            x += 50
        x = x - 50 * nbrCase
        y += 50


def vidageSprite():
    for sprites in my_sprites:
        my_sprites.remove(sprites)


liste2 = ["ressources/boutons/bouton_play.png", "ressources/boutons/bouton_easy.png",
          "ressources/boutons/bouton_medium.png", "ressources/boutons/bouton_hard.png"]


class Bouton(pygame.sprite.Sprite):
    "classe pour initilaiser les boutons et qui prend en parametres les coordonnees et le chemin"

    def __init__(self, id, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.src = id
        self.image = pygame.image.load(liste2[id]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (500, 500))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


def supprimer(groupe_sprite, bouton1, bouton2, bouton3):
    """fonction qui permet de vider l"""
    groupe_sprite.remove(bouton1)
    groupe_sprite.remove(bouton2)
    groupe_sprite.remove(bouton3)