def creer_pile() -> list:
    return []

def est_vide(p: list) -> bool:

    # Vérifie si une pile est vide
    return len(p) == 0

def empiler(p: list, v: "ELT") -> None:
    
    # Ajoute un élément au sommet de la pile
    p.append(v)
    
def depiler(p: list) -> "ELT":
    
    # Retire et renvoie l'élément au sommet de la pile
    if not est_vide(p):
        
        return p.pop()
    
    raise IndexError("Impossible de dépiler une pile vide")

    
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)