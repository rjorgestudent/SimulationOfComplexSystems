import numpy as np
import matplotlib.pyplot as plt

from PedestrianModel import Pedestrians

#===============================================================================
# Parameters
#===============================================================================
n_iterations = 100
n_individuals = 30
range_positions = [-50, 50.]
max_speed = 10.
average_speed = 7.

#===============================================================================
# Initialisation
#===============================================================================
init_positions = range_positions[0] + (range_positions[1] - range_positions[0])*np.random.rand(n_individuals, 2) 
init_velocities = -max_speed + 2.*max_speed*np.random.rand(n_individuals, 2)
desired_positions = range_positions[0] + (range_positions[1] - range_positions[0])*np.random.rand(n_individuals, 2)   #for now random positions, but they should lie on the edges
desired_speeds = np.random.normal(average_speed, 1)   #standard deviation = 1 might not be realistic

pedestrians = Pedestrians(init_positions, init_velocities, desired_positions, desired_speeds)

plt.close()
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect('equal')
plt_positions, = ax.plot(
    pedestrians.positions[:, 0], pedestrians.positions[:, 1], 'o', color='red')
fig.canvas.draw()

#===============================================================================
# Main Loop
#===============================================================================
for i_iteration in range(n_iterations):
    pedestrians.Update()
    plt_positions.set_xdata(pedestrians.positions[:, 0])
    plt_positions.set_ydata(pedestrians.positions[:, 1])
    fig.canvas.draw()
    plt.pause(0.1)
    
plt.ioff()
plt.show()  #somehow I can't close the figure window if I don't add this line...
    
