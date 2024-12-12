from pile import *
from structures import *

def creer_joueur(nom: str) -> dict:
    # Crée un joueur avec un nom, une main vide et une pile de gains vide
    return {"nom": nom, "main": creer_pile(), "gain": creer_pile()}

def perdu(joueur: dict) -> bool:
    # Vérifie si la main et la pile de gains du joueur sont toutes deux vides
    return est_vide(joueur["main"]) and est_vide(joueur["gain"])

def recuperer_gain(joueur: dict) -> None:
    # Transfère les cartes de la pile de gains vers la pile de main
    while not est_vide(joueur["gain"]):
        empiler(joueur["main"], depiler(joueur["gain"]))
        
def jouer_une_carte(joueur: dict):
    # Si le joueur n'a pas perdu
    if not perdu(joueur):
        # Si la main est vide, récupérer les cartes gagnées
        if est_vide(joueur["main"]):
            recuperer_gain(joueur)
        # Si des cartes sont disponibles, jouer la carte du sommet
        if not est_vide(joueur["main"]):
            return depiler(joueur["main"])
        
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)    