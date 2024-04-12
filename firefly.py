import random



class FireFly:
    def __init__(self):
        """
        Set up the firefly

        args:
            post
        """
        # Movement
        self.pos_X = random.uniform(0, 100)
        self.pos_Y = random.uniform(0, 100)
        self.travel_step = 1

        # Influence 
        self.radius = 1
        self.influence = 1
        self.flash = False

        # Clock
        self.clock_cycle = 12
        self.curr_time = random.randint(0,12)

    def move(self):
        """
        Firefly makes a random movement
        """
        self.pos_X += random.uniform(-1,1) * self.travel_step
        self.pos_Y += random.uniform(-1,1) * self.travel_step

    def try_flash(self):
        if self.curr_time == self.clock_cycle:
            self.curr_time = 0
            self.flash = True
        else:
            self.flash = False

    def get_flash(self):
        self.curr_time += 1
    
    def is_flash(self):
        return self.flash

    def step(self):
        self.move()
        self.curr_time += 1
        self.try_flash()

