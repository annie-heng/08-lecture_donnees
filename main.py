"""
Module servant à lire un fichier csv contenant 
uniquement des entiers.
"""
#### Imports et définition des variables globales
FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, mode = 'r', encoding = 'utf8') as f:
        l = [[int(x) for x in line.split(";")] for line in f.readlines()]
    return l

def get_list_k(data, k):
    """
    Retourne la k+1ème ligne du fichier sous forme de liste.
    """
    return data[k]

def get_first(l):
    """
    Retourne le premier élement de la liste l.
    """
    return l[0]

def get_last(l):
    """
    Retourne le dernier élement de la liste l.
    """
    return l[-1]

def get_max(l):
    """
    Retourne le maximum de la liste l.
    """
    return max(l)

def get_min(l):
    """
    Retourne le minimum de la liste l.
    """
    return min(l)

def get_sum(l):
    """
    Retourne la somme des élements de la liste l.
    """
    return sum(l)


#### Fonction principale


def main():
    """
    Fonction principale, affichant les lignes du fichier listes.csv
    """
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))

if __name__ == "__main__":
    main()
