from point import point
from queue_item import queue_item


class GrahamScan:
    def __init__(self):
        self.points = []
        self.visual_queue = []

    def set_points(self, x, y):
        for i in range(len(x)):
            p = point(x[i], y[i])
            self.points.append(p)

    # Computes the cross product of vectors <p1, p2> and <p2, p3>
    #   value of 0 means points are colinear;
    #   < 0 = clockwise;
    #   > 0 = counter clockwise
    def cross(self, p1, p2, p3):
        return (p2.x - p1.x)*(p3.y - p1.y) - (p2.y - p1.y)*(p3.x - p1.x)

    # Computes slope of line between p1 and p2
    def slope(self, p1, p2):
        return 1.0*(p1.y-p2.y)/(p1.x-p2.x) if p1.x != p2.x else float('inf')

    def convex_hull(self):
        # Find the smallest left point and remove it from the list of points
        start = min(self.points, key=lambda p: (p.x, p.y))
        self.points.pop(self.points.index(start))

        # Sort points so that traversal is from start in a counterclockwise circle.
        self.points.sort(key=lambda p: (self.slope(p, start), -p.y, p.x))

        # Add each point to the convex hull.
        # If the last 3 points make a clockwise turn, the second to last point is wrong.
        ans = [start]
        for p in self.points:
            ans.append(p)
            if self.points.index(p) > 0:
                temp_index = self.points.index(p)
                point_1 = self.points[temp_index]
                point_2 = self.points[temp_index - 1]

                # Append to the queue for animation purposes
                self.visual_queue.append(queue_item(2, point_1, point_2))

            while len(ans) > 2 and self.cross(ans[-3], ans[-2], ans[-1]) < 0:
                self.visual_queue.append(queue_item(3, ans[-2], ans[-1]))
                self.visual_queue.append(queue_item(3, ans[-2], ans[-3]))
                self.visual_queue.append(queue_item(2, ans[-1], ans[-3]))
                ans.pop(-2)
                # Append to the queue for animation purposes

            if len(ans) > 2:
                self.visual_queue.append(queue_item(3, ans[-2], ans[-1]))
            self.visual_queue.append(queue_item(1, ans[-2], ans[-1]))

        self.visual_queue.append(queue_item(1, ans[-1], ans[0]))
        return ans

    def get_visual_queue(self):
        return self.visual_queue
