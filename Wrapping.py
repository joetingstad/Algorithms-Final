from point import point
import numpy as np

# Gift wrap class holds the points and convex hull for those points
class gift_wrap:
    def __init__(self):
        self.points = []
        self.hull = None

    # Input: array of points
    # Sets the graph to hold these points
    def set_points(self, x, y):
        for i in range(len(x)):
            p = point(x[i], y[i])
            self.points.append(p)


    # Input: 3 points
    # Returns the following values:
    # 0 --> colinear
    # 1 --> clockwise
    # 2 --> counterclockwise
    def orientation(self, p, q, r):
        val = ((q.y - p.y) * (r.x - q.x)) - ((q.x - p.x) * (r.y - q.y))
        if val == 0:
            return 0
        elif val > 0:
            return 1
        else:
            return 2

    # Input: None
    # Returns convex hull of the points the object holds
    def convex_hull(self):

        # Initializes amount of points
        size = len(self.points)

        # Minimum amount of points for a convex hull is 3
        if size < 3:
            return

        # Resets the current hull the object holds
        self.hull = []

        # Finds the leftmost point
        left_most = 0
        for i in range(1, size):
            if self.points[i].x < self.points[left_most].x:
                left_most = i

        # Starts at the leftmost point
        p = left_most
        q = 0

        # print(self.points[p].x, self.points[p].y)
        # Loop does not stop until the full convex hull is made
        while True:

            # Prints point in convex hull
            # print("Convex Hull: ", self.points[p].x, self.points[p].y)

            # Adds current point to the result
            self.hull.append(self.points[p])

            # searching for point q to use as comparison to potential convex hull points
            q = (p + 1) % size

            # print("Point in Question: ", self.points[q].x, self.points[q].y)

            for i in range(size):
                # print("Check: ", self.points[i].x, self.points[i].y)
                # If i is more counterclockwise than current q, then update q
                if self.orientation(self.points[p], self.points[i], self.points[q]) == 2:
                    # print("Old point in question: ", self.points[q].x, self.points[q].y)
                    q = i
                    # print("New point in question: ", self.points[q].x, self.points[q].y)

            # q is the most counterclockwise with respect to p
            # p is set as q to be appended to the convex hull during next iteration
            p = q
            # print("P set to Q: ", self.points[p].x, self.points[p].y)
            # Returns to starting point and breaks while loop
            if p == left_most:
                break

        # Prints the points in the convex hull
        # for i in range(len(self.hull)):
        #    print(self.hull[i].x, self.hull[i].y)

        # Returns the points in the convex hull
        #return self.hull

    def get_hull(self):
        x = []
        y = []
        for point in self.hull:
            x.append(point.x)
            y.append(point.y)

        return np.c_[x, y]

