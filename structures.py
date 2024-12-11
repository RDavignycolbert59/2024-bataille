from collections import namedtuple

# Une CARTE est composée d'une valeur et d'un symbole
CARTE = namedtuple('Carte', ['valeur', 'symbole'])

# Un JOUEUR est composé d'un nom d'une main et d'un gain
JOUEUR = namedtuple("Joueur", ['nom', 'main', 'gain'])

# Un JEU est composé de deux joueurs j1 et j2 et d'un tas de carte au centre de la table
JEU = namedtuple("Jeu", ['j1', 'j2', 'tas'])