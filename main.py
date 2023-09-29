from rl_env.math_functions import MathFunctions
from simulation.config.simulation_config import SimulationConfig

import matplotlib.pyplot as plt
import numpy as np


config = SimulationConfig()
constraints = {
    "max_temp": 30,
    "min_temp": 10,
    "max_humidity": 100,
    "min_humidity": 0,
}

config.set_constraints(constraints)

simulation_params = {
    "time_interval": 10,  # minutes
    "simulation_duration": 24
}
config.set_simulation_params(simulation_params)


f = MathFunctions(config)

current_temps = np.linspace(10.1, 29.9, 400)


a = 20*2
rewards = [f.temp_reward(temp, 28, a)
           for temp in current_temps]  # Calculate rewards

# Plot the temp_reward function
plt.figure(figsize=(8, 6))
plt.plot(current_temps, rewards, label='temp_reward function')
plt.xlabel('Current Temperature')
plt.ylabel('Reward')
plt.title('Plot of temp_reward Function')
plt.legend()
plt.grid(True)
plt.show()
