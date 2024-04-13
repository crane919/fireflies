import random
import numpy as np


class FireFly():
    def __init__(self):
        """
        Set up the firefly

        args:
            post
        """
        # Movement        
        self.loc = np.array([random.uniform(0, 10), random.uniform(0, 10)])
        
        self.travel_step = 1

        # Influence 
        self.in_range = 10
        self.influence = 1
        self.flash = False

        # Clock
        self.clock_cycle = 12
        self.curr_time = random.randint(0,11)
        
    def move(self):
        """
        Firefly makes a random movement
        """
        pos_X = self.loc[0] + random.uniform(-1,1) * self.travel_step
        pos_Y = self.loc[1] + random.uniform(-1,1) * self.travel_step
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
        # self.curr_time += num_flashes
        self.curr_time += 1
        if self.curr_time > self.clock_cycle:
            self.curr_time -= self.clock_cycle
    
    def is_flash(self):
        return self.flash

    def step(self):
        self.move()
        self.curr_time += 1
        self.try_flash()

