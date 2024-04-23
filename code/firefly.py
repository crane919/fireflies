import random
import numpy as np


class FireFly():
    def __init__(self, grid_size, travel_step, in_range, clock_cycle):
        """
        Set up the firefly

        args:
            post
        """
        # Movement        
        self.loc = np.array([random.uniform(0, grid_size), random.uniform(0, grid_size)])
        self.travel_step = travel_step

        # Influence 
        self.in_range = in_range
        self.flash = False
        self.total_flashes = 0

        # Clock
        self.clock_cycle = clock_cycle
        self.curr_time = random.randint(0,self.clock_cycle-1)
        
    def move(self):
        """
        Firefly makes a random movement
        """
        pos_X = self.loc[0] + random.uniform(-1,1) * self.travel_step
        pos_Y = self.loc[1] + random.uniform(-1,1) * self.travel_step
        
        if pos_X > 15 or pos_X < 0 or pos_Y > 15 or pos_Y < 0:
            np.array([random.uniform(0, 15), random.uniform(0, 15)])
        else:
            self.loc = np.array([pos_X, pos_Y])

    def try_flash(self):
        """
        Seeing if firefly is ready to flash
        """
        if self.curr_time == self.clock_cycle:
            self.curr_time = 0
            self.flash = True
        else:
            self.flash = False

    def get_flash(self, num_flashes):
        self.curr_time += num_flashes
        # self.curr_time += 1

    
    def is_flash(self):
        return self.flash

    def step(self):
        self.move()
        self.curr_time += 1
        self.try_flash()
