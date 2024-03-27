from manipulation_histogramme import *

def regrouper_points(data, max_iterations=500):
    """
    Divise un ensemble de points dans un plan 2D en un nombre défini de groupes en utilisant l'algorithme K-means.
    Arguments :
    data (numpy.ndarray): Un tableau 2d numpy représentant l'ensemble de données à partitionner.
    k (int): Le nombre de groupes à identifier dans l'ensemble de données.
    max_iterations (int): Le nombre maximal d'itérations que l'algorithme exécutera. La valeur par défaut est 50.
    Retourne :
    numpy.ndarray: Un tableau numpy 1D où chaque élément correspond à l'indice du centre le plus proche pour chaque point de l'ensemble de données.
    """
    k = 2

    # Initialisation aléatoire des centres
    centroids = np.empty((k, data.shape[1]))

    centroids[0] = [1, 1, 1, 1]

    centroids[1] = data[np.random.choice(data.shape[0] - 1) + 1]

    if k > 2:
        centroids[2:] = data[np.random.choice(data.shape[0], k - 2, replace=False)]

    converged = False
    iteration = 0

    while not converged and iteration < max_iterations:
        # Calcul des distances de chaque point par rapport aux centres
        distances = np.array([np.array([calculer_distance_1(point, centroid) for centroid in centroids]) for point in data])

        # Attribution des groupes en fonction des distances minimales
        groups = np.argmin(distances, axis=1)

        # Mise à jour des centres
        new_centroids = np.array([data[groups == i].mean(axis=0) for i in range(k)])

        # Vérification de la convergence
        if np.all(centroids == new_centroids):
            converged = True
        else:
            centroids = new_centroids

        iteration += 1

    return groups

# Exemple d'utilisation
if __name__ == "__main__":
    # Génération de données aléatoires pour l'exemple
    #np.random.seed(0)

    data = np.array([[4, 4, 3, 3],
                     [3, 4, 2, 2],
                     [3, 0, 2, 3],
                     [1, 0, 2, 1],
                     [2, 0, 2, 0],
                     [1, 4, 2, 3],
                     [3, 4, 2, 3],
                     [2, 3, 2, 2]])

    # Partitionnement des données en utilisant K-means
    groups = regrouper_points(data)

    print("Affectation des groupes pour chaque point :")
    print(groups)
