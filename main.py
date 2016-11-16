import numpy as np
import matplotlib.pyplot as plt
import geometries
from WallAvoidingSwarm import WallAvoidingSwarm
import time


n_iterations = 100
n_individuals = 40

geometry = geometries.box_with_hole()

init_positions = np.random.rand(n_individuals, 2) * 8 + 1
init_speeds = 0.05 * (np.random.rand(n_individuals, 2) * 8 + 1)

swarm = WallAvoidingSwarm(
    wills="some sort of array will go here",
    geometry=geometry,
    init_positions=init_positions,
    init_speeds=init_speeds)

fig = plt.figure()
plt.xlim([-3, 13])
plt.ylim([-3, 13])
ax = fig.add_subplot(111)
ax.set_aspect('equal')
ax.plot(geometry[:, 0], geometry[:, 1], 'o', markersize=2, color='black')
fig.canvas.draw()
plt_positions, = ax.plot(
    swarm.positions[:, 0], swarm.positions[:, 1], 'o', color='red')
fig.canvas.draw()
plt.pause(0.005)

for _ in range(n_iterations):
    swarm.update()
    plt_positions.set_xdata(swarm.positions[:, 0])
    plt_positions.set_ydata(swarm.positions[:, 1])
    fig.canvas.draw()
    plt.pause(0.005)  # ugly solution but I can't get it to work otherwise
