import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from kmeans import KMeansClustering


class VisualizeKMeansClustering:
    def __init__(self):
        self.markers = ["o", "x", "v", "<", ">"]
        self.model = KMeansClustering()
        self.plots = []
        self.fig, self.ax = plt.subplots()

        # initial plot
        clusters = self.model.iterate()
        centroids = self.model.centroids
        for i in range(len(clusters)):
            cluster = clusters[i]
            x, y = cluster[:, 0], cluster[:, 1]
            (plot,) = self.ax.plot(x, y, self.markers[i], label=i)
            self.plots.append(plot)

        x_cent, y_cent = centroids[:, 0], centroids[:, 1]
        (self.init_plot,) = self.ax.plot(x_cent, y_cent, ".", label="Centroids")
        self.plots.append(self.init_plot)
        self.ax.set_title("K-Means Algorithm (Iteration 1)")
        self.ax.legend()

    def get_init_plot(self):
        return self.init_plot

    def update(self, frame):
        clusters = self.model.iterate()
        centroids = self.model.centroids

        for j in range(len(clusters)):
            cluster = clusters[j]
            x, y = cluster[:, 0], cluster[:, 1]
            self.plots[j].set_data(x, y)

        x_cent, y_cent = centroids[:, 0], centroids[:, 1]
        self.plots[-1].set_data(x_cent, y_cent)

        self.ax.set_title(f"K-Means Algorithm (Iteration {self.model.iteration})")

        self.fig.gca().relim()
        self.fig.gca().autoscale_view()


if __name__ == "__main__":
    visualizer = VisualizeKMeansClustering()
    animation = FuncAnimation(
        visualizer.fig,
        visualizer.update,
        interval=1000,
        init_func=visualizer.get_init_plot,
    )
    plt.show()
