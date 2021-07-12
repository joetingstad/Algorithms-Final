import random


class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

points_1k = []
points_2k = []

for i in range(0, 100000):
    x = random.randint(-10000, 10000)
    y = random.randint(-10000, 10000)

    points_1k.append(
        point(x, y)
    )

for i in range(0, 200000):
    x = random.randint(-10000, 10000)
    y = random.randint(-10000, 10000)

    points_2k.append(
        point(x, y)
    )

outfile_1k = open('100k.txt', 'w')
outfile_2k = open('200k.txt', 'w')

for point in points_1k:
    outfile_1k.write(str(point.x) + ' ' + str(point.y) + '\n')

for point in points_2k:
    outfile_2k.write(str(point.x) + ' ' + str(point.y) + '\n')