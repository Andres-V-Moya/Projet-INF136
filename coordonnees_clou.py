from transformation_geometrique import *


def calculer_coordonnees_clou(A, B, C, D, E):
    """
    Retourner les coordonnées d'un clou selon la paramétrisation illustrée dans la Figure 1 dans l'énoncé du projet.

    Arguments:
        A, B, C, D, E (float): Dimensions spécifiques du clou.
    Retourne:
        (liste): Les coordonnées des points ainsi que leur nom.
    """
    # Définition des points selon les dimensions réçus.
    pt_0 = ('pt_0', (-B / 2, C / 2))
    pt_1 = ('pt_1', (-B / 2, -C / 2))
    pt_2 = ('pt_2', (-B / 2 - D, -A / 2))
    pt_3 = ('pt_3', (-B / 2 - D, A / 2))
    pk_2 = ('pk_2', (B / 2, C / 2))
    pk_0 = ('pk_0', (B / 2 + E, 0))
    pk_1 = ('pk_1', (B / 2, -C / 2))

    cord_clou = [pt_0, pt_1, pt_2, pt_3, pk_2, pk_0, pk_1]
    return cord_clou


def appliquer_transormation_clou(points_clou, center_rotation, angle_rotation,
                                 direction_inclinaison, angle_inclinaison, axe_reflexion):
    """
    Appliquer les transformation géometriques: réflexion, rotation et inclinaison à tous les points clés.
    Arguments:
        points_clou (list): Une liste de tuples qui contient le nom du point
        et les coordonnées du point dans un plan 2D.
        center_rotation (tuple): Le centre de rotation pour la transformation de rotation.
        angle_rotation (float): L'angle de rotation en degrés.
        angle_inclinaison (float): L'anlge d'inclinaison en degrés.
        direction_inclinaison (str): La direction d'inclinaison ('x' ou 'y').
        axe_reflexion (str): L'axe de réflexion ('x' ou 'y').
    Retourne:
        (tuple): Trois liste de tuples qui correspond aux coordonnées des points clés apres
         l'application d'unedes transformations (réflexion, rotation, inclinaison).
    """
    reflexion = []
    rotation = []
    inclinaison = []

    # Ajouter le nom du point ainsi que les coordonnées suite à leur transformation à un liste.
    for i in range(len(points_clou)):
        reflexion.append((points_clou[i][0], calculer_reflexion_point(points_clou[i][1], axe_reflexion)))
        rotation.append((points_clou[i][0], calculer_rotate_point(points_clou[i][1], angle_rotation, center_rotation)))
        inclinaison.append((points_clou[i][0], calculer_inclinaison_point(points_clou[i][1], angle_inclinaison,
                            direction_inclinaison)))
    return reflexion, rotation, inclinaison
