import numpy as np
import matplotlib.pyplot as plt
import geometries
from DumbSwarm import DumbSwarm
from time import sleep


n_individuals = 20

geometry = geometries.box_with_hole()

init_positions = np.random.rand(n_individuals, 2) * 8 + 1
init_speeds = np.random.rand(n_individuals, 2) * 8 + 1

swarm = DumbSwarm(
    wills="some sort of array will go here",
    geometry=geometry,
    init_positions=init_positions,
    init_speeds=init_speeds)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(geometry[:, 0], geometry[:, 1], s=2, color='black')
ax_xs, ax_ys = ax.scatter(swarm.positions[:, 0], swarm.positions[:, 1])
fig.canvas.draw()

'''
plt.scatter(pts[:, 0], pts[:, 1], s=2, color='black')
time.sleep(1)
plt.scatter(swarm.positions[:, 0], swarm.positions[:, 1], color='red')
plt.xlim([-1, 11])
plt.ylim([-1, 11])
plt.plot()

'''
