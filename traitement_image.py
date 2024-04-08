import numpy as np
import matplotlib.pyplot as plt

def rgb_to_gry(chemin_vers_image_org, chemin_vers_image_ng):
    """
    Transfomer une image en couleur en une nouvelle image en niveaux de gris.

    Arguments:
        chemin_vers_image_org (str): Le chemin de l'image en couleur.
        chemin_vers_image_ng (str): Le chemin où l'image résultatnte en gris sera sauvegarder.

    Retourne:
        None
    """
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

    Arguments:
        tableau (numpy.ndarray): Un tableau 2D NumPy représentant une image en niveaux de gris.
        i (int): Coordonée du pixel selon les lignes du tableau.
        j (int): Coordonée du pixel selon les colonnes du tableau.

    Retourne
        (int): Une décimale qui représente au le voisinage de la coordonée (i,j).
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

        # Si les valeurs voisines ne sont pas dans le tableau on donne la valeur de 0.
        else:
            motif_binaire += '0'

    # Conversion du motif binaire en valeur décimale
    motif_decimal = int(motif_binaire, 2)

    return motif_decimal

def appliquer_transformation_1(tableau):
    """
    Calcul de la valeur entière correspondant au motif binaire pour chaque valeur du tableau.

    Arguments:
        tableau (numpy.ndarray): Un tableau 2D NumPy représentant une image en niveaux de gris.

    Retourne:
        (numpy.ndarray): Un tableau 2D NumPy résultant de la transformation 1.
    """
    resultat = np.zeros_like(tableau)

    # Parcours du tableau pour chaque valeur
    for i in range(1, tableau.shape[0]-1):
        for j in range(1, tableau.shape[1]-1):
            resultat[i, j] = motif_voisin(tableau, i, j)

    return resultat

### Il manque la description et les arguments et le retourne
def log_voisin(tableau, i, j, rayon):
    """
        Transformer l'intensité en valeur plus simple et plus significative.

    Arguments:
        tableau (numpy.ndarray): Un tableau 2D NumPy représentant une image en niveaux de gris.
        i (int): Coordonée du pixel selon les lignes du tableau.
        j (int): Coordonée du pixel selon les colonnes du tableau.j:
        rayon (int): Un entier spécificant le rayon du voisinage à considérer pour chaque pixel de l'image.

    Retourne:
        (float): Un entier représentant l'intensité du pixel.
    """

    log_ho = np.log10(1.0 + np.abs(tableau[i, j + rayon] - 2 * tableau[i, j] + tableau[i, j - rayon]))

    log_ver = np.log10(1.0 + np.abs(tableau[i + rayon, j] - 2 * tableau[i, j] + tableau[i - rayon, j]))

    log_diag = np.log10(1.0 + np.abs(tableau[i - rayon, j + rayon] - 2 * tableau[i, j] + tableau[i + rayon, j - rayon]))

    valeur_tot = int(log_ho + log_ver + log_diag)

    return valeur_tot

### Il manque les arguments et le retourne
def appliquer_transformation_2(image_gris, rayon):
    """
        Transformer les données visuelles complexes d'une image en ensembles de caractéristiques plus simples et
         plus significatives
    Arguments:
        image_gris (numpy.ndarray): Un tableau 2D NumPy rerpésentant une image en niveaux de gris.
        rayon (int): Un entier spécificant le rayon du voisinage.

    Retourne:
        (numpy.ndarray): Un tableau 2D NumPy résultant de la transformation 2.
    """
    resultat = np.zeros_like(image_gris)

    # Parcours du tableau pour chaque valeur
    for i in range(rayon, image_gris.shape[0]-rayon):
        for j in range(rayon, image_gris.shape[1]-rayon):
            resultat[i, j] = log_voisin(image_gris, i, j, rayon)

    return resultat
