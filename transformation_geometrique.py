import math
import numpy as np


def calculer_reflexion_point(reflechir_point, axe_reflexion):
    """
    Retourner la réflextion d'un point (x,y) selon un axe spécifié (l'absisse ou l'ordonnée).

    Arguments:
        reflechir_point (tuple): Les coordonnées du point à réfléchir.
        axe_reflexion (str): L'axe de réflexion.
    Retourne:
        (tuple): Les coordonnées du point réflechi selon l'absisse ou l'ordonnée.
    """
    # Réfléchir le point selon l'abscisse
    if axe_reflexion == 'x':
        return reflechir_point[0], reflechir_point[1] * -1
    # Réfléchir le point selon l'ordonnée
    if axe_reflexion == 'y':
        return reflechir_point[0] * -1, reflechir_point[1]


def calculer_rotate_point(pivoter_point, angle_rot, centre=(0, 0)):
    """
    Retourner les coordonnées d'un point suite à sa rotation par rapport à un centre reçu

    Arguments:
        pivoter_point (tuple): Les coordonnées du point à pivoter.
        angle_rot (float): L'angle de rotation en degrés.
        centre (tuple, optionnel): Coordonnées du centre de rotation.
    Retourne:
        (tuple): Les coordonnées du point suite à la rotation
    """
    angle_rad = math.radians(angle_rot)

    # Tuple de la différence entre le centre donné et l'origine (0,0)
    diff_centre = (0 - centre[0], 0 - centre[1])

    # Translation du point à pivoter pour avoir son centre de rotation à l'origine
    point_transla_origine = ([pivoter_point[0] + diff_centre[0],
                             pivoter_point[1] + diff_centre[1]])

    # Matrice de rotation p/r à l'axe Z
    rotation = ([math.cos(angle_rad), math.sin(angle_rad) * -1],
                [math.sin(angle_rad), math.cos(angle_rad)])

    # Transformer la matrice résultante de la rotation selon l'origine (0,0) en tuple
    point_pivote_origine = tuple(np.dot(rotation, point_transla_origine))

    # Translation du point pivoté pour avoir son centre de rotation de retour à celui reçu
    point_transla_centre = (point_pivote_origine[0] - diff_centre[0], point_pivote_origine[1] - diff_centre[1])

    return round(point_transla_centre[0], 2), round(point_transla_centre[1], 2)


def calculer_inclinaison_point(incliner_point, angle_incli, direction_incli):
    """
    Retourner les coordonnées d'un point suite à une inclinaison.

    Arguments:
        incliner_point (tuple): Les coordonnées du point à incliner.
        angle_incli (float): L'angle d'inclinaison en degrés.
        direction_incli (str): La direction de l'inclinaison.
    Retourne:
        (tuple): Les coordonnées du point suite à l'inclinaison.
    """
    angle_rad = math.radians(angle_incli)

    # Coordonnées du point à pivoter en matrice
    point_matrice = ([incliner_point[0],
                      incliner_point[1]])

    # Inclinaison horizontale
    if direction_incli == 'x':
        # Matrice d'inclinaison en direction de l'abscisse
        rotation_hori = ([1, math.tan(angle_rad)],
                         [0, 1])

        # Transformer la matrice résultante en tuple
        point_incline = tuple(np.dot(rotation_hori, point_matrice))

        return round(point_incline[0], 2), round(point_incline[1], 2)

    if direction_incli == 'y':
        # Matrice d'inclinaison en direction de l'ordonnée
        rotation_verti = ([1, 0],
                          [math.tan(angle_rad), 1])

        # Transformer la matrice résultante en tuple
        point_incline = tuple(np.dot(rotation_verti, point_matrice))

        return round(point_incline[0], 2), round(point_incline[1], 2)