import matplotlib.pyplot as plt


class Plotter:
    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot()

    def plot_scatter_points(self, points):

        x = [p[0] for p in points]
        y = [p[1] for p in points]
        self.ax.scatter(x, y)

    def plot_line_points(self, points):
        x = [p[0] for p in points]
        y = [p[1] for p in points]
        self.ax.plot(x, y)

    def show(self):
        plt.show()
