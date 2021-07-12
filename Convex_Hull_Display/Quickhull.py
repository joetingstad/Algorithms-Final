# Inspired from: https://www.geeksforgeeks.org/quickhull-algorithm-convex-hull/
from point import point
from queue_item import queue_item
import numpy as np


class Quickhull:
    def __init__(self):
        self.hull = []
        self.points = []
        self.visual_queue = []

    def set_points(self, x, y):
        for i in range(len(x)):
            p = point(x[i], y[i])
            self.points.append(p)

    def find_side(self, p1, p2, p):
        val = ((p.y - p1.y) * (p2.x - p1.x)) - ((p2.y - p1.y) * (p.x - p1.x))
        if val > 0:
            return 1
        if val < 0:
            return -1
        return 0

    def line_dist(self, p1, p2, p):
        return abs(((p.y - p1.y) * (p2.x - p1.x)) - ((p2.y - p1.y) * (p.x - p1.x)))

    def add_to_queue(self, line_type, p1, p2):
        if line_type == 1:
            self.visual_queue.append(queue_item(line_type, p1, p2))
        elif line_type == 2:
            self.visual_queue.append(queue_item(line_type, p1, p2))
        elif line_type == 3:
            self.visual_queue.append(queue_item(line_type, p1, p2))
        elif line_type == 4:
            self.visual_queue.append(queue_item(line_type, p1, p2))

    def quick_hull(self, n, p1, p2, side):
        ind = -1
        max_dist = 0

        for i in range(n):
            temp = self.line_dist(p1, p2, self.points[i])
            if self.find_side(p1, p2, self.points[i]) == side and temp > max_dist:
                ind = i
                max_dist = temp
                self.add_to_queue(2, p1, self.points[ind])
                self.add_to_queue(2, p2, self.points[ind])
                self.add_to_queue(3, p1, p2)
                self.add_to_queue(3, p1, p2)

        if ind == -1:
            self.hull.append(p1)
            self.hull.append(p2)
            self.add_to_queue(1, p1, p2)
            return
        else:
            self.add_to_queue(2, p1, self.points[ind])
            self.add_to_queue(2, p2, self.points[ind])
            self.add_to_queue(3, p1, p2)
            self.add_to_queue(3, p1, p2)

        self.quick_hull(n, self.points[ind], p1, -self.find_side(self.points[ind], p1, p2))
        self.quick_hull(n, self.points[ind], p2, -self.find_side(self.points[ind], p2, p1))

    def convex_hull(self):
        n = len(self.points)

        if n < 3:
            return

        min_x = 0
        max_x = 0
        for i in range(1, n):
            if self.points[i].x < self.points[min_x].x:
                min_x = i
            if self.points[i].x > self.points[max_x].x:
                max_x = i

        self.add_to_queue(2, self.points[min_x], self.points[max_x])
        self.quick_hull(n, self.points[min_x], self.points[max_x], 1)
        self.add_to_queue(4, self.points[min_x], self.points[max_x])
        self.quick_hull(n, self.points[min_x], self.points[max_x], -1)

    def get_visual_queue(self):
        return self.visual_queue

