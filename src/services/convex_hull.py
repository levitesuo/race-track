import numpy as np
import math


class ConvexHullMaker:
    def __init__(self) -> None:
        self._hull = []

    def quick_hull(self, points):
        p = sorted(points, key=lambda p: (p[0], p[1]), reverse=True)

        a = p.pop(0)
        b = p.pop()
        self._hull = [a, b]
        smaller, bigger = self._divide_points(points, a, b)

        self._find_hull(smaller, a, b)
        self._find_hull(bigger, b, a)

        return self._hull

    def _divide_points(self, points, p, q):
        x1, y1 = p
        x2, y2 = q

        slope = (y2 - y1) / (x2 - x1)
        b = slope * x1 - y1

        def line(x):
            return x * slope + b

        smaller = []
        bigger = []

        for point in points:
            if line(point[0]) < point[1]:
                smaller.append(point)
            else:
                bigger.append(point)

        return smaller, bigger

    def _find_hull(self, sk, p, q):

        def distanse_from_line_qp(point):
            x0, y0 = point
            x1, y1 = p
            x2, y2 = q
            return abs((y2-y1)*x0-(x2-x1)*y0+x2*y1-y2*x1)/math.sqrt((y2-y1)**2+(x2-x1)**2)

        def if_not_in_triangle(point, v1, v2, v3):
            def sign(p1, p2, p3):
                return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

            d1 = sign(point, v1, v2)
            d2 = sign(point, v2, v3)
            d3 = sign(point, v3, v1)

            has_neg = d1 < 0 or d2 < 0 or d3 < 0
            has_pos = d1 > 0 or d2 > 0 or d3 > 0

            return (has_neg and has_pos)

        if not len(sk):
            return

        # From the given set of points in Sk, find farthest point, say C, from segment PQ.
        max_distanse = 0
        c = 0
        for point in sk:
            d = distanse_from_line_qp(point)
            if d > max_distanse:
                max_distanse = d
                c = point

        # Add point C to convex hull at the location between P and Q
        i = 0
        while i < len(self._hull) and (self._hull[i][0] != p[0] or self._hull[i][1] != p[1]):
            i += 1
        hull = self._hull[0:i+1] + [c] + self._hull[i+1:]
        self._hull = hull.copy()

        # Three points P, Q, and C partition the remaining points of Sk into 3 subsets: S0, S1, and S2
        # where S0 are points inside triangle PCQ, S1 are points on the right side of the oriented
        # line from P to C, and S2 are points on the right side of the oriented line from C to Q.

        s0 = filter(lambda p0: if_not_in_triangle(p0, p, c, q), sk)
        s1, _ = self._divide_points(s0, p, c)
        _, s2 = self._divide_points(s0, c, q)

        self._find_hull(s1, p, c)
        self._find_hull(s2, c, q)
