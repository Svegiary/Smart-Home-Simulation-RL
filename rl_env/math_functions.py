import math

from simulation.config.simulation_config import SimulationConfig


class MathFunctions:

    def __init__(self, config: SimulationConfig):
        self.config = config

    def temp_reward(self, current_temp: float, target_temp: float, a: float):

        if current_temp >= 10 and current_temp <= target_temp:
            if current_temp < 10.2:
                print("current_temp", current_temp)
            return math.log(current_temp - (target_temp - 20), 2)

        elif current_temp > target_temp and current_temp <= self.config.max_temp:
            print("current_temp", current_temp)

            return math.log(30 + (target_temp - 10) - current_temp, 2)
