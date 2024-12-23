import numpy as np
import random

from services.logger import Logger
from services.plotter import Plotter
from services.convex_hull import ConvexHullMaker

logger = Logger()
plotter = Plotter()
huller = ConvexHullMaker()

size_of_map = 1000
num_of_points = 20
seed = random.randint(0, 100)

random.seed(seed)
logger.log(f"The seed for this run in {seed}")

points = [np.array((random.randint(1, size_of_map-1),
                   random.randint(1, size_of_map-1))) for _ in range(num_of_points)]

# logger.log(points)

hull = huller.quick_hull(points)

plotter.plot_scatter_points(points)
plotter.plot_line_points(hull)
logger.log(hull)
plotter.show()
