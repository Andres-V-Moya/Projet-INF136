import numpy as np
import matplotlib.pyplot as plt

def rgb_to_gry(chemin_vers_image_org, chemin_vers_image_ng):

    # Chargement de l'image originale
    img = plt.imread(chemin_vers_image_org)

    # Dimension de l'image a traiter
    height, width, _ = img.shape

    # Creation d'un tableau ayant les memes dimensions que l'image et ayant les trois canaux de couleur par pixel.
    gry_img = np.zeros((height, width, 3), dtype=np.uint8)

    # Conversion des couleurs RGB en niveau de gris
    for y in range(height):
        for x in range(width):
            # Calcul de la moyenne des couleurs RGB
            valeur_gry = np.mean(img[y, x])

            # Attribution des niveau de gris a la nouvelle image
            gry_img[y, x] = valeur_gry

    # Enregistrement de l'image
    plt.imsave(chemin_vers_image_ng, gry_img, cmap='gray')

def motif_voisin(tableau, i, j):
    """
    Calcul du motif binaire pour une valeur donnée et conversion en valeur décimale.
    """
    motif_binaire = ''

    # Valeur centrale
    central = tableau[i, j]

    # Coordonnées des voisins
    neighbors = [(i-1, j-1), (i-1, j), (i-1, j+1),
                 (i, j+1),              (i+1, j+1),
                 (i+1, j), (i+1, j-1), (i, j-1)]

    # Comparaison des valeurs des voisins avec la valeur centrale
    for neighbor_i, neighbor_j in neighbors:
        # Verification si les valeurs sont dans le tableau
        if 0 <= neighbor_i < tableau.shape[0] and 0 <= neighbor_j < tableau.shape[1]:
            neighbor_value = tableau[neighbor_i, neighbor_j]
            motif_binaire += '1' if neighbor_value >= central else '0'
        else:
            motif_binaire += '0'  # Outline values treated as zeros

    # Conversion du motif binaire en valeur décimale
    motif_decimal = int(motif_binaire, 2)

    return motif_decimal

def appliquer_transformation_1(tableau):
    """
    Calcul de la valeur entière correspondant au motif binaire pour chaque valeur du tableau.
    """
    resultat = np.zeros_like(tableau)

    # Parcours du tableau pour chaque valeur
    for i in range(1, tableau.shape[0]-1):
        for j in range(1, tableau.shape[1]-1):
            resultat[i, j] = motif_voisin(tableau, i, j)

    return resultat