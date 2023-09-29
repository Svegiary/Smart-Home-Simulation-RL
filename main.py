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
    "min_luminance": 0.0,
    "max_luminance": 1.0
}

config.set_constraints(constraints)

simulation_params = {
    "time_interval": 10,  # minutes
    "simulation_duration": 24
}
config.set_simulation_params(simulation_params)


current_temps = np.linspace(0.01, 0.99, 400)


rewards = [MathFunctions.luminance_reward(temp, 0.8, config)
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
