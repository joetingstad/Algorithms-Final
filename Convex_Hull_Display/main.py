from matplotlib import pyplot as plt
import numpy as np
import weakref
from matplotlib.animation import FuncAnimation
from point import point
from queue_item import queue_item
import csv
import random
from Quickhull import Quickhull
from Wrapping import GiftWrap
from Graham import GrahamScan


# Visuals 0 & 1 are the x and y values of the points
# 2 - Quickhull Queue
# 3 - Graham Scan Queue
# 4 - Gift Wrapping Queue
visuals = [[], [], [], [], []]

# Option to read in points from a text file
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


# Function that creates n number of points in a range of -x to x
def get_points():
    for i in range(100):
        x = random.randint(-10000, 10000)
        visuals[0].append(x)
        y = random.randint(-10000, 10000)
        visuals[1].append(y)


# Creates the points specified in the function and stores x and y values
get_points()
X = np.array(visuals[0])
Y = np.array(visuals[1])

# Creates the figure where animations happen as well as titles
fig, axs = plt.subplots(1, 3)
fig.suptitle('Convex Hull Algorithms')
axs[0].set_title('Quickhull')
axs[1].set_title('Graham Scan')
axs[2].set_title('Gift Wrapping')

# Plots the points on all the animation graphs
axs[0].plot(X, Y, 'ko-', lw=0)
axs[1].plot(X, Y, 'ko-', lw=0)
axs[2].plot(X, Y, 'ko-', lw=0)


# Function to run all the convex hull functions
# Retrieves visual queues for algorithms and stores them in visuals array
def generate_convex_hulls(x, y):

    # Numpy array to hold the points
    p = np.c_[x, y]

    convex_hull = Quickhull()
    convex_hull.set_points(x, y)
    convex_hull.convex_hull()
    visuals[2] = convex_hull.get_visual_queue()

    convex_hull = GrahamScan()
    convex_hull.set_points(x, y)
    convex_hull.convex_hull()
    visuals[3] = convex_hull.get_visual_queue()

    convex_hull = GiftWrap()
    convex_hull.set_points(x, y)
    convex_hull.convex_hull()
    visuals[4] = convex_hull.get_visual_queue()


# Runs the generation function specified above
generate_convex_hulls(X, Y)

# Global variables for the wrapping algorithm animation to use
global prev_gw, last_blue_index
prev_gw = 0
last_blue_index = -1


# Runs the quickhull animations
def quickhull_animate(i):
    if visuals[2] and i > 1:
        temp = visuals[2].pop(0).get_line_format()
        if temp[0] == 1:
            axs[0].plot([temp[1], temp[2]], [temp[3], temp[4]], 'r-')
        elif temp[0] == 2:
            axs[0].plot([temp[1], temp[2]], [temp[3], temp[4]], 'b-')
        elif temp[0] == 3:
            axs[0].lines.pop(len(axs[0].lines) - 1)
        elif temp[0] == 4:
            axs[0].lines.pop(1)


# Runs the graham scan animations
def graham_scan_animate(i):
    if visuals[3] and i > 1:
        temp = visuals[3].pop(0).get_line_format()
        if temp[0] == 1:
            axs[1].plot([temp[1], temp[2]], [temp[3], temp[4]], 'r-')
        elif temp[0] == 2:
            axs[1].plot([temp[1], temp[2]], [temp[3], temp[4]], 'b-')
        elif temp[0] == 3:
            axs[1].lines.pop(-1)


# Runs the gift wrapping animations
def wrapping_animate(i):
    global prev_gw, last_blue_index
    if visuals[4] and i > 1:
        temp = visuals[4].pop(0).get_line_format()
        if temp[0] == 1:
            if last_blue_index != len(axs[2].lines) - 1:
                axs[2].lines.pop(last_blue_index)
            axs[2].lines.pop(len(axs[2].lines) - 1)

            last_blue_index = -1
            prev_gw = 1

            axs[2].plot([temp[1], temp[2]], [temp[3], temp[4]], 'r-')
        elif temp[0] == 2:

            # Deletes green line if previous
            # Deletes previous blue line
            if prev_gw == 2 or prev_gw == 3:
                axs[2].lines.pop(len(axs[2].lines) - 1)
            if last_blue_index != len(axs[2].lines) and last_blue_index != -1:
                axs[2].lines.pop(last_blue_index)

            last_blue_index = len(axs[2].lines) - 1
            prev_gw = 2

            axs[2].plot([temp[1], temp[2]], [temp[3], temp[4]], 'b-')
            last_blue_index = len(axs[2].lines) - 1

        elif temp[0] == 3:
            if prev_gw == 3:
                axs[2].lines.pop(len(axs[2].lines) - 1)
            prev_gw = 3
            axs[2].plot([temp[1], temp[2]], [temp[3], temp[4]], 'g-')


# Animation function to run all the algorithm animation functions at once
def animate(i):
    # Offset to wait until animations starts
    # Decrease i for animation to run sooner (min == 0)
    # Increase i for animation to run later
    if i > 50:
        quickhull_animate(i)
        wrapping_animate(i)
        graham_scan_animate(i)


# Takes the biggest number of frames for the algorithms
# Allows the animation to run until all algorithms are finished
frame_nums = max(len(visuals[2]), len(visuals[3]), len(visuals[4]))

# Increase interval value to make the animation slower
# Decrease interval value to make the animation faster
ani = FuncAnimation(fig, animate, frames=frame_nums, interval=50, blit=False)

# Runs the animation
plt.tight_layout()
plt.show()