import matplotlib.pyplot as plt

class Graphs:
    def create_points_plot(self, pairs_of_points):
        x = list()
        y = list()
        for i in range(len(pairs_of_points)):
            x.append(pairs_of_points[i][0])
            y.append(pairs_of_points[i][1])

        plt.scatter(x=x, y=y)
        plt.scatter(x=x[0], y=y[0], c='r')
        plt.plot(x, y)
        plt.show()


