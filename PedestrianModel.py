import numpy as np

class Pedestrians():
    
    def __init__(self, init_positions, init_velocities, desired_positions, desired_speeds):
        self.positions = init_positions
        self.velocities = init_velocities
        self.desired_positions = desired_positions
        self.desired_speeds = desired_speeds
        
    def Update(self):
        self.Update_Velocities()
        self.Update_Positions()
        
    def Update_Velocities(self):
        desired_velocities = self.Get_Desired_Velocities()
        #call more update functions here
        
        self.velocities += desired_velocities

    def Update_Positions(self):
        self.positions += self.velocities   #actually times time step. We should consider setting it not to 1, so we can convert our numerical velocities to realistic values
        #insert if clause for periodic boundary conditions
        
    def Get_Desired_Velocities(self):
        desired_direction = self.desired_positions - self.positions
        desired_direction = desired_direction / np.linalg.norm(desired_direction)
        desired_velocities = self.desired_speeds * desired_direction
        
        return desired_velocities
    
    #define more update functions here        