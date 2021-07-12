# https://iq.opengenus.org/gift-wrap-jarvis-march-algorithm-convex-hull/

import time
import random
#from reader import feed

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def __gt__(self, other):
        if self.x > other.x:
            return True
        elif self.x == other.x and self.y > other.y:
            return True
        return False
 
    def __le__(self, other):
        if self.x < other.x:
            return True
        elif self.x == other.x and self.y < other.y:
            return True
        elif self.x == other.x and self.y == other.y:
            return True
        else:
            return False

# Gift wrap class holds the points and convex hull for those points    
class gift_wrap:
    def __init__(self):
        self.points = None
        self.hull = None

    # Input: array of points
    # Sets the graph to hold these points
    def set_points(self, points):
        self.points = points

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
        
        #print(self.points[p].x, self.points[p].y)
        # Loop does not stop until the full convex hull is made 
        while True:

            # Prints point in convex hull
            #print("Convex Hull: ", self.points[p].x, self.points[p].y)
            
            # Adds current point to the result 
            self.hull.append(self.points[p])

            # searching for point q to use as comparison to potential convex hull points
            q = (p + 1) % size
            
            #print("Point in Question: ", self.points[q].x, self.points[q].y)
            
            for i in range(size):
                #print("Check: ", self.points[i].x, self.points[i].y)
                # If i is more counterclockwise than current q, then update q
                if self.orientation(self.points[p], self.points[i], self.points[q]) == 2:
                    #print("Old point in question: ", self.points[q].x, self.points[q].y)
                    q = i
                    #print("New point in question: ", self.points[q].x, self.points[q].y)

            # q is the most counterclockwise with respect to p
            # p is set as q to be appended to the convex hull during next iteration 
            p = q
            #print("P set to Q: ", self.points[p].x, self.points[p].y)
            # Returns to starting point and breaks while loop 
            if p == left_most:
                break

        # Prints the points in the convex hull 
        #for i in range(len(self.hull)):
        #    print(self.hull[i].x, self.hull[i].y)

        # Returns the points in the convex hull
        return self.hull

# Reads in file and creates array for points 
f = open("100k.txt", 'r')
points_100k = []

for i in range(0, 100000):
    line = f.readline().strip()
    x = 0
    y = 0
    temp = 0
    neg_flag = 0
    for char in line:
        if char == '-':
            neg_flag = 1
        elif char.isnumeric():
            temp *= 10
            temp += 10
        else:
            if neg_flag == 1:
                temp *= -1
            x = temp
            temp = 0
    if neg_flag == 1:
        temp *= -1
    y = temp
    points_100k.append(point(x, y))
f.close()

# Creates graph object 
graph = gift_wrap()
graph.set_points(points_100k)

# Times the algorithm speed 
tic = time.perf_counter()
graph.convex_hull()
toc = time.perf_counter()
print("Time: ", toc - tic, " second")