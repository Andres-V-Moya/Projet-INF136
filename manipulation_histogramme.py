import numpy as np


def petit_tableau(tableau, i, j, w):

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

    m, n = tableau.shape
    resultat = []

    # Parcours du tableau pour chaque valeur
    for i in range(w, m + 1):
        for j in range(w, n + 1):
            resultat.append(petit_tableau(tableau, i, j, w))

    resultat = np.array(resultat)
    return resultat

def calculer_distance_1(histo1, histo2):
    distance = np.sum((histo1 - histo2) ** 2)

    distance = distance ** 0.5

    return round(distance, 2)

def calculer_distance_2(histo1, histo2):

    distance = np.sum((abs(histo1 - histo2)))

    return round(distance, 2)

if __name__ == '__main__':

    histo1 = np.array([3, 2, 2, 2])

    histo2 = np.array([3, 1.5, 2, 2.5])
    #histo2 = np.array([3.5, 1, 2, 2.5])

    print(calculer_distance_1(histo1, histo2))