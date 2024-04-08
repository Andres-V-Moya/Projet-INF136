import numpy as np


def petit_tableau(tableau, i, j, w):
    """

    Args:
        tableau:
        i:
        j:
        w:

    Returns:

    """
    valeur_max = tableau.max()
    m, n = tableau.shape

    # coordonne des valeurs du petit tableau
    indices = [(x, y) for x in range(i - w, i)
               for y in range(j - w, j)
               if 0 <= x < m and 0 <= y < n]

    # Extraction des valeurs dans le petit tableau
    ptit_tableau = [tableau[x, y] for x, y in indices]

    # Histogramme des valeurs extraites
    hist, _ = np.histogram(ptit_tableau, bins=[0, valeur_max / 4, valeur_max / 2, (3 * valeur_max) / 4, valeur_max],
                           range=(0, valeur_max))

    return hist


def calculer_histogramme(tableau, w):
    """
    Génère un histogramme pour chaque pixel de l'image en utilisant le voisinage du pixel.

    Arguments:
        tableau (numpy.ndarray): Un tableau 2D NumPy représentant une image.
        w (int): La taille du carré de voisinage autour de chaque pixel pour lequel l'histogramme est calculé.

    Retourne:
        (numpy.ndarray): Un tableau 2D NumPy où chaque ligne représente un histogramme pour
         le carré correspondant de l'image.
    """
    m, n = tableau.shape
    resultat = []

    # Parcours du tableau pour chaque valeur
    for i in range(w, m + 1):
        for j in range(w, n + 1):
            resultat.append(petit_tableau(tableau, i, j, w))

    resultat = np.array(resultat)
    return resultat


def calculer_distance_1(histo1, histo2):
    """
    Calculer la distance entre deux histogrammes.

    Arguments:
        histo1 (numpy.ndarray): Histogramme 1 sous forme de tableau 1D NumPy.
        histo2 (numpy.ndarray): Histogramme 2 sous forme de tableau 1D NumPy.

    Retourne:
        (float): La distance entre les deux histogrammes.
    """
    distance = np.sum((histo1 - histo2) ** 2)

    distance = distance ** 0.5

    return round(distance, 2)

def calculer_distance_2(histo1, histo2):
    """
        Calculer la distance entre deux histogrammes.

        Arguments:
            histo1 (numpy.ndarray): Histogramme 1 sous forme de tableau 1D NumPy.
            histo2 (numpy.ndarray): Histogramme 2 sous forme de tableau 1D NumPy.

        Retourne:
            (float): La distance entre les deux histogrammes.
    """
    distance = np.sum((abs(histo1 - histo2)))

    return round(distance, 2)