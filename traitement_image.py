import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def appliquer_rgb_to_gry(chemin_vers_image_org, chemin_vers_image_ng):

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


def appliquer_transformation_1(image_gris):

    img = Image.open(image_gris)

    width, height = img.size

    middle_x = width // 2
    middle_y = height // 2

    middle_pixel = img.getpixel((middle_x, middle_y))

    binary_img = Image.new('1', (width, height))

    for y in range(height):
        for x in range(width):
            if (x, y) != (middle_x, middle_y):
                pixel_value = img.getpixel((x, y))
                if pixel_value > middle_pixel:
                    binary_img.putpixel((x, y), 1)
                else:
                    binary_img.putpixel((x, y), 0)

    binary_img.show()

if __name__ == '__main__':
    image_gris = "image_niveaux_de_gris.jpg"
    appliquer_transformation_1(image_gris)
