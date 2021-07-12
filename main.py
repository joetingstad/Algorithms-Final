from matplotlib import pyplot as plt
import numpy as np
import weakref
from matplotlib.animation import FuncAnimation
from point import point
from queue_item import queue_item
import csv
import random
from Wrapping import GiftWrap
from Graham import GrahamScan


# Visuals 0 & 1 are the x and y values of the points
# 2 - Gift Wrapping Queue
# 3 - Quickhull Queue
# 4 - Graham Scan Queue
visuals = [[], [], [], [], []]
"""
def get_points():
    f = open("points.txt", 'r')

    num_points = int(f.readline().strip())

    for i in range(num_points):
        line = f.readline().strip()

        temp = 0
        neg_flag = 0
        for char in line:
            if char.isnumeric():
                temp *= 10
                temp += int(char)
            elif char == '-':
                neg_flag = 1
            else:
                if neg_flag == 1:
                    temp *= -1
                    neg_flag = 0
                visuals[0].append(temp)
                temp = 0
        if neg_flag == 1:
            temp *= -1
        visuals[1].append(temp)
"""


def get_points():
    for i in range(0, 50):
        x = random.randint(-1000, 1000)
        visuals[0].append(x)
        y = random.randint(-1000, 1000)
        visuals[1].append(y)


get_points()
fig, axs = plt.subplots(1, 3)
#fig.suptitle('Convex Hull Algorithms')
fig.set_size_inches(9, 9)
axs[0].set_title('Quickhull')
axs[1].set_title('Gift Wrapping')
axs[2].set_title('Graham Scan')
X = np.array(visuals[0])
Y = np.array(visuals[1])

axs[0].plot(X, Y, 'ko-', lw=0)
axs[1].plot(X, Y, 'ko-', lw=0)
axs[2].plot(X, Y, 'ko-', lw=0)


def generate_convex_hulls(x, y):

    # Numpy array to hold the points
    p = np.c_[x, y]

    # Uploads the visual instructions for the gift wrapping algorithm
    convex_hull = GiftWrap()
    convex_hull.set_points(x, y)
    convex_hull.convex_hull()
    visuals[2] = convex_hull.get_visual_queue()

    convex_hull = GrahamScan()
    convex_hull.set_points(x, y)
    convex_hull.convex_hull()
    visuals[3] = convex_hull.get_visual_queue()


generate_convex_hulls(X, Y)

global prev_gw, last_blue_index
prev_gw = 0
last_blue_index = -1


def wrapping_animate(i):
    global prev_gw, last_blue_index
    if visuals[2] and i > 1:
        temp = visuals[2].pop(0).get_line_format()
        if temp[0] == 1:
            if last_blue_index != len(axs[1].lines) - 1:
                axs[1].lines.pop(last_blue_index)
            axs[1].lines.pop(len(axs[1].lines) - 1)

            last_blue_index = -1
            prev_gw = 1

            axs[1].plot([temp[1], temp[2]], [temp[3], temp[4]], 'r-')
        elif temp[0] == 2:

            # Deletes green line if previous
            # Deletes previous blue line
            if prev_gw == 2 or prev_gw == 3:
                axs[1].lines.pop(len(axs[1].lines) - 1)
            if last_blue_index != len(axs[1].lines) and last_blue_index != -1:
                axs[1].lines.pop(last_blue_index)

            last_blue_index = len(axs[1].lines) - 1
            prev_gw = 2

            axs[1].plot([temp[1], temp[2]], [temp[3], temp[4]], 'b-')
            last_blue_index = len(axs[1].lines) - 1

        elif temp[0] == 3:
            if prev_gw == 3:
                axs[1].lines.pop(len(axs[1].lines) - 1)
            prev_gw = 3
            axs[1].plot([temp[1], temp[2]], [temp[3], temp[4]], 'g-')


def graham_scan_animate(i):
    if visuals[3] and i > 1:
        temp = visuals[3].pop(0).get_line_format()
        print(temp[0])
        if temp[0] == 1:
            axs[2].plot([temp[1], temp[2]], [temp[3], temp[4]], 'r-')
        elif temp[0] == 2:
            axs[2].plot([temp[1], temp[2]], [temp[3], temp[4]], 'b-')
        elif temp[0] == 3:
            axs[2].lines.pop(-1)


def animate(i):
    wrapping_animate(i)
    graham_scan_animate(i)


ani = FuncAnimation(fig, animate, frames=1000, interval=50, blit=False)
plt.tight_layout()
plt.show()
