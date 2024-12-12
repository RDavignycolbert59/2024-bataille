from structures import *

VALEURS  = ['7', '8', '9', '10', 'V', 'D', 'R', 'As']
SYMBOLES = ['♦', '♥', '♠', '♣']

def creer_carte(v: int, s: int) -> dict:
    # Crée une carte avec une valeur et un symbole
    return {"valeur": VALEURS[v], "symbole": SYMBOLES[s]}

def comparer_carte(c1: dict, c2: dict) -> int:
    # Compare deux cartes en fonction de leurs valeurs
    valeur_c1 = VALEURS.index(c1["valeur"])
    valeur_c2 = VALEURS.index(c2["valeur"])
    if valeur_c1 < valeur_c2:
        return 1
    elif valeur_c1 > valeur_c2:
        return -1
    else:
        return 0

def afficher_carte(c: dict) -> str:
    # Renvoie une chaîne de caractères représentant la carte
    return f"{c['valeur']} de {c['symbole']}"

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)