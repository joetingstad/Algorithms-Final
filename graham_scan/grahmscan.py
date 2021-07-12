import time

my_q = []

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class line_def:
    def __init__(self, line_type, x1, x2, y1, y2):
        self.line_type = line_type
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

class queue_item:
    def __init__(self, type, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.type = type

    def get_line_format(self):
        line = [self.type, self.p1.x, self.p2.x, self.p1.y, self.p2.y]
        return line

def grahamscan(points):
    # Computes the cross product of vectors <p1, p2> and <p2, p3>
    #   value of 0 means points are colinear; 
    #   < 0 = clockwise; 
    #   > 0 = counter clockwise
    def cross(p1, p2, p3):
        return (p2.x - p1.x)*(p3.y - p1.y) - (p2.y - p1.y)*(p3.x - p1.x)

    # Computes slope of line between p1 and p2
    def slope(p1, p2):
        return 1.0*(p1.y-p2.y)/(p1.x-p2.x) if p1.x != p2.x else float('inf')

    # Find the smallest left point and remove it from the list of points
    start = min(points, key=lambda p: (p.x, p.y))
    points.pop(points.index(start))

    # Sort points so that traversal is from start in a counterclockwise circle.
    points.sort(key=lambda p: (slope(p, start), -p.y, p.x))

    # Add each point to the convex hull.
    # If the last 3 points make a clockwise turn, the second to last point is wrong. 
    ans = [start]
    for p in points:
        ans.append(p)
        if points.index(p) > 0:
            temp_index = points.index(p)
            point_1 = points[temp_index]
            point_2 = points[temp_index - 1]

            # Append to the queue for animation purposes
            my_q.append(
                queue_item(1, point_1, point_2)
            )
        while len(ans) > 2 and cross(ans[-3], ans[-2], ans[-1]) < 0:
            ans.pop(-2)
            # Append to the queue for animation purposes
            my_q.append(
                queue_item(2, ans[-2], ans[-1])
            )
    return ans


if __name__ == '__main__':
    # Open test case file
    input_file = open('100k.txt', 'r')
    input_lines = input_file.readlines()
    input_file.close()

    # Read in list of points and store in points_list
    points_list = []
    for line in input_lines:
        line_as_list = line.split(' ')
        points_list.append(
            point(int(line_as_list[0]), int(line_as_list[1]))
        )

    # Run algorithm
    starttime = time.time()
    temp = grahamscan(points_list)
    print("Grahamscan runtime: " + str(time.time() - starttime))

    # Print points on the hull
    outfile = open('output.txt', 'w')
    for point in temp:
        outfile.write('(' + str(point.x) + ', ' + str(point.y) + ')\n')
    outfile.close()