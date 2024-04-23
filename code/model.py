from firefly import FireFly
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
from IPython.display import clear_output
from matplotlib.animation import FuncAnimation



class Firefly_Model():
    """
    Represents a Firefly Syncronizaton Model.
    """

    def __init__(self, grid_size=15, num_agents=50, travel_step=3, in_range=8, clock_cycle=10):
        """
        Create a new Firefly model
        Args:
            grid_size (int): the size of the grid (rows and columns)
            num_agents (int): the number of agents to generate. Defaults to 100.
        """
        self.grid_size = grid_size
        self.num_agents = num_agents
        self.agents = []
        
        self.travel_step = travel_step
        self.in_range = in_range
        self.clock_cycle = clock_cycle

        self.overall_time = 0
        self.time_series = []
        self.firefly_series = []
        self.blink_series = []

        self.make_agents()

    
    def make_agents(self):
        """
        Create the initial agents for this model

        Returns:
          a list of initial Agents to use in this model
        """

        for i in range(self.num_agents):
            self.agents.append(FireFly(self.grid_size, self.travel_step, self.in_range, self.clock_cycle))
    
    def step(self):
        self.total_flashes = 0
        times = []
        self.handle_flash()
        for agent in self.agents:
            agent.try_flash()
        for agent in self.agents:
            agent.step()
            times.append(agent.curr_time)
        print(times)
        self.record()
        self.overall_time+=1

        
    def draw(self):
        """
        Draws the current state of the model
        """
        flash_coords = []
        non_flash_coords = []
        
        for agent in self.agents:
            if agent.is_flash():
                flash_coords.append([agent.loc[0], agent.loc[1]])
            else:
                non_flash_coords.append([agent.loc[0], agent.loc[1]])

        plt.scatter([coord[0] for coord in flash_coords], [coord[1] for coord in flash_coords], color='yellow')
        plt.scatter([coord[0] for coord in non_flash_coords], [coord[1] for coord in non_flash_coords], color='black')
            
    
    def handle_flash(self):
        flashing_agents_locs = []
        non_flashing_agents = []
        blink_count = 0
        for firefly in self.agents:
            if firefly.is_flash():
                flashing_agents_locs.append(firefly.loc)
                blink_count += 1
            else:
                non_flashing_agents.append(firefly)
                
        print("Flashing:", len(flashing_agents_locs), "Not flashing:", len(non_flashing_agents))
        
        self.total_flashes = blink_count
        print("Total Blinks: ", self.total_flashes)
        self.blink_series.append(self.total_flashes)
        
        if len(flashing_agents_locs) != 0:
            for non_flashing_firefly in non_flashing_agents:
                arr = np.array(flashing_agents_locs) - non_flashing_firefly.loc
                arr_2 = np.linalg.norm(arr, axis=1)
                count = 0
                for num in arr_2:
                    if num < non_flashing_firefly.in_range:
                        count += 1
                if count > 0:
                    non_flashing_firefly.get_flash(count)
                    if non_flashing_firefly.curr_time > non_flashing_firefly.clock_cycle:
                        non_flashing_firefly.curr_time = 0 
                    
    
    def handle_flash2(self):
        # Go through all fireflies
        for firefly in self.agents:
            # If the firefly is flashing
            if firefly.is_flash():
                # Go through all fireflies
                for other_firefly in self.agents:
                    # Select all none flashing fireflies
                    if not other_firefly.is_flash():
                        # See if the two fireflies are close enough
                        if self.close_enough(firefly, other_firefly):
                            # Receive flash
                            other_firefly.get_flash()
        

    def close_enough(self, firefly1, firefly2):
        """
        firefly1 = flashing
        firefly2 = not flashing
        """
        (x1, y1) = firefly1.loc
        (x2, y2) = firefly2.loc
        
        dist = np.sqrt((x2-x1)**2 + (y2-y1)**2)
        
        if dist <= firefly1.in_range:
            return True
        return False
        
    def run(self, frames=1000):
        for _ in range(frames):
            self.step()
            if self.total_flashes == self.num_agents:
                break



    def animate(self):
        """
        Animate the model
        """
        fig, ax = plt.subplots()

        def update(frame):
            ax.clear()  # Clear the previous frame
            self.step()  # Advance the simulation
            self.draw()  # Draw the updated state of the model

        ani = FuncAnimation(fig, update, frames=range(100), interval=100)

        plt.show()
        
    def record(self):
        self.time_series.append(self.overall_time)
        temp = []
        for firefly in self.agents:
            temp.append(firefly.curr_time)
        self.firefly_series.append(temp)
    

    def plot_fireflies_over_time(self):
        per_flys = np.transpose(np.array(self.firefly_series))

        for fly in per_flys:
            plt.plot(self.time_series, fly)
        plt.xlabel("Overall Time")
        plt.ylabel("Firefly Clock")
        plt.title("Firefly Behavior Over Time")
        plt.legend()
        plt.show()

    def plot_blink(self, title="Firefly Behavior Over Time"):

        plt.plot(self.time_series, self.blink_series, ".")
        plt.xlabel("Overall Time")
        plt.ylabel("BLink COunt")
        plt.title(title)
        plt.legend()
        plt.show()



test_model = Firefly_Model(grid_size=30, num_agents=50, travel_step=6, in_range=16, clock_cycle=10)
test_model.run(frames=10000)
test_model.plot_blink()
#test_model.plot_fireflies_over_time()


