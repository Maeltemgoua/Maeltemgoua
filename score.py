
def enregistrer_score(pseudo, score_partie):
        """"fonction pour enregistrer le score qui prend en paramètre le pseudo et le score
        on ouvre le fichier score qui contient un dictionnaire, on regarde si notre pseudo est dedans
        si oui on compare les deux scores et on garde le meilleur.
        Sinon on ajoute notre pseudo et notre score aux dictionnaires"""
        with open("scores.txt", "r") as fichier:
            scores = eval(fichier.read())
            if pseudo in scores.keys():
                meilleur_score = scores[pseudo]
                if score_partie > meilleur_score:
                    scores[pseudo] = score_partie
                else:
                    scores[pseudo] = meilleur_score
            else :
                scores[pseudo] = score_partie
        with open("scores.txt", "w") as fichier:
            fichier.write(str(scores))
