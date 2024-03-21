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
    centrale = tableau[i, j]

    # Coordonnées des voisins
    voisin = [(i-1, j-1), (i-1, j), (i-1, j+1),
              (i, j+1), (i+1, j+1), (i+1, j),
              (i+1, j-1), (i, j-1)]

    # Comparaison des valeurs des voisins avec la valeur centrale
    for voisin_i, voisin_j in voisin:
        # Verification si les valeurs sont dans le tableau
        if 0 <= voisin_i < tableau.shape[0] and 0 <= voisin_j < tableau.shape[1]:
            valeur_voisin = tableau[voisin_i, voisin_j]
            motif_binaire += '1' if valeur_voisin >= centrale else '0'
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


def log_voisin(tableau, i, j, rayon):

    log_ho = np.log10(1.0 + np.abs(tableau[i, j + rayon] - 2 * tableau[i, j] + tableau[i, j - rayon]))

    log_ver = np.log10(1.0 + np.abs(tableau[i + rayon, j] - 2 * tableau[i, j] + tableau[i - rayon, j]))

    log_diag = np.log10(1.0 + np.abs(tableau[i - rayon, j + rayon] - 2 * tableau[i, j] + tableau[i + rayon, j - rayon]))

    valeur_tot = int(log_ho + log_ver + log_diag)

    return valeur_tot


def appliquer_transformation_2(tableau, rayon):
    """
    Calcul de la valeur entière correspondant au motif binaire pour chaque valeur du tableau.
    """
    resultat = np.zeros_like(tableau)

    # Parcours du tableau pour chaque valeur
    for i in range(rayon, tableau.shape[0]-rayon):
        for j in range(rayon, tableau.shape[1]-rayon):
            resultat[i, j] = log_voisin(tableau, i, j, rayon)

    return resultat
