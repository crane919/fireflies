from firefly import FireFly
import numpy as np
import matplotlib as plt


class Firefly_Model():
    """
    Represents a Firefly Syncronizaton Model.
    """

    def __init__(self, grid_size=100, num_agents=100, **agent_params):
        """
        Create a new Firefly model
        Args:
            grid_size (int): the size of the grid (rows and columns)
            num_agents (int): the number of agents to generate. Defaults to 100.
            agent_params: parameters to pass to Agent
        """
        self.grid_size = grid_size
        self.num_agents = num_agents
        self.agent_params = agent_params
        self.agents = []
        self.make_agents()
    
    def make_agents(self):
        """
        Create the initial agents for this model

        Returns:
          a list of initial Agents to use in this model
        """

        for i in range(self.num_agents):
            self.agents.append(FireFly())
    
    def step(self):
        for agent in self.agents:
            agent.step()
        self.handle_flash()

        
    def draw(self):
        """
        Draws the current state of the model
        """
        xs, ys = self.get_coords()
        
        if FireFly.is_flashing:
            # draw agent as yellow
            self.points = plt.plot(xs, ys, '.', color='yellow')[0]
        else:
            # draw agent as bug-color
            self.points = plt.plot(xs, ys, '.', color='red')[0]
        
    def get_coords(self):
        """
        Gets the coordinates of the agents.

        returns:

        """
        # flashing_agent_locs = np.array()
        # non_flashing_agent_locs = np.array()
        # for agent in self.agents:
        #     if agent.is_flashing:
        #         flashing_agent_locs.append(agent.locs)
        #     else:
        #         non_flashing_agent_locs.append(agent.locs)
        # return flashing_agent_locs, non_flashing_agent_locs
        agent_locs = np.array()
        for agent in self.agents:
            agent_locs.append(agent.loc)
        return agent_locs
    
    def handle_flash(self):
        # flashing_agent_locs, non_flashing_agent_locs = self.get_coords()
        # for non_flashing_firefly in non_flashing_agent_locs:
        flashing_agents_locs = np.array()
        non_flashing_agents = np.array()
        for firefly in self.agents:
            if firefly.is_flash():
                flashing_agents_locs.append(firefly.loc)
            else:
                non_flashing_agents.append(firefly)
        
        for non_flashing_firefly in non_flashing_agents:
            arr = flashing_agents_locs - non_flashing_firefly.loc
            arr_2 = np.linalg.norm(arr, axis=1)
            count = 0
            for num in arr_2:
                if num < non_flashing_firefly.in_range:
                    count += 1
            non_flashing_firefly.get_flash(count)            



test_model = Firefly_Model()
test_model.make_agents()
