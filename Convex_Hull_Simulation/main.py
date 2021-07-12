import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import sin, cos
import random

visuals = [[], [], []]


def get_points():
    for i in range(5):
        x = random.randint(-10, 10)
        visuals[0].append(x)
        y = random.randint(-10, 10)
        visuals[1].append(y)


def data_gen():
    gen_list = ([t, t] for t in np.arange(-10, 10, 0.1))
    return gen_list


def init():
    ax.set_ylim(-10, 10)
    ax.set_xlim(-10, 10)
    return point

X = visuals[0]
Y = visuals[1]

fig, ax, = plt.subplots()
point, = ax.plot(visuals[0], visuals[1], 'go')
point.set_data(visuals[0], visuals[1])
ax.grid()


def run(data):
    t, y = data
    ax.figure.canvas.draw()
    point.set_data(t, y)
    return point


ani = animation.FuncAnimation(fig, run, data_gen, init_func=init, interval=10)
plt.show()



