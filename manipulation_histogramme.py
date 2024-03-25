import numpy as np
import math

def petit_tableau(tableau, i, j, sub_array_size):
    max_value = tableau.max()
    m, n = tableau.shape
    half_size = math.ceil(sub_array_size / 2)

    # Generate indices for the sub-array
    indices = [(x, y) for x in range(i - half_size, i + half_size)
               for y in range(j - half_size, j + half_size)
               if 0 <= x < m and 0 <= y < n]

    # Extract values from the larger array using the generated indices
    ptit_tableau = [tableau[x, y] for x, y in indices]

    hist, _ = np.histogram(ptit_tableau, bins=[0, max_value / 4, max_value / 2, (3 * max_value) / 4, max_value],
                           range=(0, max_value))

    return hist

def calculer_histogramme(tableau, sub_array_size):
    """
    Calcul de la valeur entière correspondant au motif binaire pour chaque valeur du tableau.
    """
    m, n = tableau.shape
    resultat = []

    # Parcours du tableau pour chaque valeur
    for i in range(m):
        for j in range(n):
            resultat.append(petit_tableau(tableau, i, j, sub_array_size))

    resultat = np.array(resultat)
    print(resultat)

def calculer_distance_1(histo1, histo2):
    distance = np.sum((histo1 - histo2) ** 2)

    distance = distance ** 0.5

    return round(distance, 2)

def calculer_distance_2(histo1, histo2):

    distance = np.sum((abs(histo1 - histo2)))

    return round(distance, 2)


if __name__ == '__main__':
    tableau = np.array([[255, 160, 10, 49],
                        [20, 170, 1, 121],
                        [30, 233, 230, 100],
                        [255, 23, 155, 88]])

    sub_array_size = 2  # Define the size of the sub-arrays

    calculer_histogramme(tableau, sub_array_size)