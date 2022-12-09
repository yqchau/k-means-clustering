import numpy as np


class KMeansClustering:
    def __init__(self, k=3, n=1000, d=2, mean=0, std=100):
        """
        k: number of clusters
        n: number of randomly sampled points
        d: dimension of each point
        mean: mean of the normal distribution of the randomly sampled points
        std: standard deviation of the normal distribution of the randomly sampled points
        """
        self.k = k
        self.data = np.random.normal(mean, std, (n, d))
        self.centroids = np.random.normal(mean, std, (k, d))
        self.clusters = [None for i in range(k)]
        self.iteration = 0

    def iterate(self):
        """
        1) calculate nearest centroid for each point
        2) reassign each point to the nearest centroid's clusters
        3) recalculate centroid coordinates
        """

        new = np.stack(
            [
                np.sum((self.data - centroid) ** 2, axis=-1)
                for centroid in self.centroids
            ]
        )
        idx = np.argmin(new, axis=0)

        for cluster in range(self.k):
            self.clusters[cluster] = self.data[idx == cluster]  # update clusters
            self.centroids[cluster] = np.mean(
                self.clusters[cluster], axis=0
            )  # update centroids

        self.iteration += 1

        return (*self.clusters,)
