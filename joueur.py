from pile import *
from structures import *

def creer_joueur(nom:str) -> "JOUEUR":
    """
        La main d'un joueur est une pile
        Les gain d'un joueur sont dans une pile
        
        :tests:
        >>> j = creer_joueur("DAVID")
        >>> j.nom
        "DAVID"
        >>> est_vide(j.main)
        True
        >>> est_vide(j.gain)
        True
    """
    pass

def perdu(joueur:"JOUEUR") -> bool:
    """
        Un joueur a perdu quand sa main est vide et qu'il n'a pas de cartes gagnées
        
        :tests:
        >>> j = creer_joueur("DAVID")
        >>> perdu(j)
        True
        >>> empiler(j.main(creer_carte(0, 0)))
        >>> perdu(j)
        False
    """
    pass

def recuperer_gain(joueur:"JOUEUR") -> None:
    """
        Récupère les cartes gagnées précédemment
        On vide la pile de gain dans la pile de main
        
        :tests:
        >>> j = creer_joueur("DAVID")
        >>> empiler(j.gain, creer_carte(0, 0))
        >>> recuperer_gain(j)
        >>> est_vide(j.gain)
        True
        >>> depiler(j.main)
        Carte(valeur='7', symbole='♦')
    """
    pass
        
def jouer_une_carte(joueur):
    """
        Si le joueur n'a pas perdu :
            - S'il n'a plus de carte dans sa main : il peut récupérer celles gagnées
            - jouer la carte disponible
            
        :tests:
        >>> j = creer_joueur("DAVID")
        >>> jouer(j)
        >>> empiler(j.gain, creer_carte(0, 0))
        >>> jouer(j)
        Carte(valeur='7', symbole='♦')
    """       
    pass
        
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)    