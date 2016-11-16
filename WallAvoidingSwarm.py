import numpy as np


class WallAvoidingSwarm():

    def __init__(self, wills, geometry, init_positions, init_speeds):
        self.wills = wills
        self.geometry = geometry
        self.positions = init_positions
        self.speeds = init_speeds

    def update(self):
        self._update_speeds()
        self._update_positions()

    def _update_speed(self, i):
        wall_nearby = False
        for j in range(self.geometry.shape[0]):
            dist = np.linalg.norm(self.geometry[j, :] - self.positions[i, :])
            if dist < 0.25:
                wall_nearby = True
                break
        if wall_nearby:
            self.speeds[i, :] *= -1
            self.speeds[i, :] += (np.random.rand(1, 2) - 0.5).reshape(2,) * 0.02

    def _update_speeds(self):
        for i in range(self.speeds.shape[0]):
            self._update_speed(i)

    def _update_positions(self):
        self.positions += self.speeds
