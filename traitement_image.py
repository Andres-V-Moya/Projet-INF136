import numpy as np
import matplotlib.pyplot as plt


def appliquer_rgb_to_gry(chemin_vers_image_org, chemin_vers_image_ng):

    img = plt.imread(chemin_vers_image_org)

    height, width, _ = img.shape

    gry_img = np.zeros((height, width, 3), dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            # Calculate average of RGB components
            gray_value = np.mean(img[y, x])

            # Assign grayscale value to each pixel
            gry_img[y, x] = gray_value

    plt.imsave(chemin_vers_image_ng, gry_img, cmap='gray')
