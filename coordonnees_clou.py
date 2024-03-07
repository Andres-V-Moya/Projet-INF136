from transformation_geometrique import *

def calculer_coordonnees_clou(A, B, C, D, E):
    """
       Retourner les coordonnées d'un clou selon la paramétrisation illustrée dans la Figure 1 dans l'énoncé du projet.

       Arguments:
           A, B, C, D, E (float): Dimensions spécifiques du clou.
       Retourne:
           (liste): Les coordonnées des points ainsi que leur nom.
    """
    pt_0 = ('pt_0', (-B / 2, C / 2))
    pt_1 = ('pt_1', (-B / 2, -C / 2))
    pt_2 = ('pt_2', (-B / 2 - D, -A / 2))
    pt_3 = ('pt_3', (-B / 2 - D, A / 2))
    pk_2 = ('pk_2', (B / 2, C / 2))
    pk_0 = ('pk_0', (B / 2 + E, 0))
    pk_1 = ('pk_1', (B / 2, -C / 2))
    cord_clou = [pt_0, pt_1, pt_2, pt_3, pk_2, pk_0, pk_1]
    return cord_clou