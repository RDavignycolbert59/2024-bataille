from jeu import *

def main():
    jeu = creer_jeu("DAVID", "ORDI")
      
    while not termine(jeu):
        c1, c2 = jouer(jeu) # Ici c1 et c2 ne sont jamais égaux à None car la partie n'est pas terminée
        
        if comparer_carte(c1, c2) == 1: # Le joueur 1 gagne
            recuperer_tas(jeu, jeu.j1)
        elif comparer_carte(c1, c2) == -1: # Le joueur 2 gagne
            recuperer_tas(jeu, jeu.j2)
        else: # Bataille
            if not termine(jeu):
                jouer(jeu) # Inutile de connaître la valeur de ces cartes. Le tas n'est pas vidé, on recommence au début.
       
    # En sortie de boucle, il y a forcément un gagnant
    if perdu(jeu.j1):
        print(f"Le gagnant est {jeu.j2.nom}")
    else:
        print(f"Le gagnant est {jeu.j1.nom}")
        
                    
