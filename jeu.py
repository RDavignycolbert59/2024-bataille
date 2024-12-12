from carte import *
from joueur import *
from random import shuffle

def creer_jeu(nom_j1: str, nom_j2: str) -> list:
    # Crée un jeu avec les noms des joueurs sous forme de liste
    
    return [{"nom": nom_j1, "main": creer_pile(), "gain": creer_pile()},
                  {"nom": nom_j2, "main": creer_pile(), "gain": creer_pile()}]
    # On crée les cartes
    cartes = []
    for s in range(4):
        for v in range(8):
            cartes.append(creer_carte(v, s))    
    shuffle(cartes) # On mélange
    
    # On crée les joueurs
    j1 = creer_joueur(nom_j1)
    j2 = creer_joueur(nom_j2)

    res = JEU(j1, j2, creer_pile()) # On crée le jeu
    distribuer(cartes, res) # On distribue aux joueurs
    
    return res

def termine(jeu: "JEU") -> bool:
    # Le jeu est terminé si l'un des deux joueurs a perdu
    return perdu(jeu["j1"]) or perdu(jeu["j2"])
    
def distribuer(cartes: list, jeu: "JEU") -> None:
    # Distribue les cartes entre les deux joueurs d'un jeu
    while cartes:
        empiler(jeu["j1"]["main"], cartes.pop())
        if cartes:  # Vérifie qu'il reste encore des cartes
            empiler(jeu["j2"]["main"], cartes.pop())

def recuperer_tas(jeu: "JEU", joueur: dict) -> None:
    # Le joueur récupère toutes les cartes du tas et les ajoute à ses gains
    while not est_vide(jeu["tas"]):
        empiler(joueur["gain"], depiler(jeu["tas"]))
    
def jouer(jeu: "JEU") -> None:
    # Simule une partie où chaque joueur envoie une carte dans le tas si possible
    if not termine(jeu):
        for joueur in [jeu["j1"], jeu["j2"]]:
            if not perdu(joueur):
                carte = jouer_une_carte(joueur)
                if carte is not None:
                    empiler(jeu["tas"], carte)
 
    c1 = jouer_une_carte(jeu.j1)
    c2 = jouer_une_carte(jeu.j2)
    
    if c1 != None and c2 != None:
        empiler(jeu.tas, c1)
        empiler(jeu.tas, c2)
        
    return c1, c2

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True) 
    