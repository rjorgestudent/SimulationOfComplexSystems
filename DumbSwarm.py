import numpy as np


class DumbSwarm():

    def __init__(self, wills, geometry, init_positions, init_speeds):
        self.wills = wills
        self.geometry = geometry
        self.positions = init_positions
        self.speeds = init_speeds

    def update(self):
        self.positions += self.speeds
