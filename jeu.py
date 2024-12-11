from carte import *
from joueur import *
from random import shuffle

def creer_jeu(nom_j1:str, nom_j2:str) -> list:
    """
        Le tas est une pile       
    """   
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

def termine(jeu:"JEU") -> bool:
    """
        Le jeu est terminé quand le joueur 1 a perdu OU quand le joueur 2 a perdu
        
        :tests:
        >>> j = creer_jeu("DAVID", "ORDI")
        >>> termine(j)
        False
        >>> j = JEU(creer_joueur("DAVID"), creer_joueur("ORDI"))
        >>> terminer(j)
        True
    """
    pass
    
def distribuer(cartes:list, jeu:"JEU") -> tuple:
    """
        Distribue les cartes entre les deux joueurs d'un jeu
    """   
    while cartes != []:
        empiler(jeu.j1.main, cartes.pop())
        empiler(jeu.j2.main, cartes.pop())

def recuperer_tas(jeu, joueur):
    """
        Le joueur récupère le tas de carte
        
        :tests:
        >>> j = creer_jeu("DAVID", "ORDI")
        >>> carte = depiler(j.j1.main)
        >>> empiler(j.tas, carte)
        >>> recuperer_tas(j, j.j2)
        >>> est_vide(j.tas)
        True
        >>> depiler(j.j2.gain) == carte
        True
    """
    pass
    
def jouer(jeu):
    """
        Simule une partie        
        Chaque joueur envoie une carte dans le tas si possible
    """        
    c1 = jouer_une_carte(jeu.j1)
    c2 = jouer_une_carte(jeu.j2)
    
    if c1 != None and c2 != None:
        empiler(jeu.tas, c1)
        empiler(jeu.tas, c2)
        
    return c1, c2

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True) 
    