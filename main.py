from rl_env.math_functions import MathFunctions
from rl_env.reward_calculation import RewardCalculation
from rl_env.reward_normalization.normalization import Normalization
from rl_env.reward_normalization.normalization_strategy import MinMaxNormalization, ZScoreNormalization
from simulation.config.simulation_config import SimulationConfig

import matplotlib.pyplot as plt
import numpy as np

from simulation.preferences.simulation_preferences import Preferences


config = SimulationConfig()
constraints = {
    "max_temp": 30.1,
    "min_temp": 10.1,
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

preferences = Preferences()

pref = {
    "target_temp": 25,
    "target_humidity": 60,
    "target_luminance": 0.8

}

preferences.set_preferences(pref)
"""
temp_reward = MathFunctions.temp_reward(25, preferences.target_temp, config)
print("temp reward ", temp_reward)
temp_edges = [MathFunctions.temp_reward(config.min_temp, preferences.target_temp, config),
              MathFunctions.temp_reward(
                  config.max_temp, preferences.target_temp, config),
              MathFunctions.temp_reward(preferences.target_temp, preferences.target_temp, config)]
min_temp_reward = min(temp_edges)
max_temp_reward = max(temp_edges)

print("min temp reward ", min_temp_reward)
print("max temp reward ", max_temp_reward)


normiliaze_rewards = Normalization()
strategy = MinMaxNormalization()
normiliaze_rewards.set_strategy(strategy)
print("normalizded temp reward ", strategy.normalize(
    temp_reward, max_temp_reward, min_temp_reward))


humidity_reward = MathFunctions.humidity_reward(
    60, preferences.target_hum, config)
humidity_edges = [
    MathFunctions.humidity_reward(
        config.min_humidity, preferences.target_hum, config),
    MathFunctions.humidity_reward(
        config.max_humidity, preferences.target_hum, config),
    MathFunctions.humidity_reward(
        preferences.target_hum, preferences.target_hum, config)
]
min_humidity_reward = min(humidity_edges)
max_humidity_reward = max(humidity_edges)

print("min humidity reward ", min_humidity_reward)
print("max humidity reward ", max_humidity_reward)

print("normiliazed humidity reward ", strategy.normalize(
    humidity_reward, max_humidity_reward, min_humidity_reward))


luminance_reward = MathFunctions.luminance_reward(
    0.1, preferences.target_luminance, config)


luminance_edges = [
    MathFunctions.luminance_reward(
        config.min_luminance, preferences.target_luminance, config),
    MathFunctions.luminance_reward(
        preferences.target_luminance, preferences.target_luminance, config),
    MathFunctions.luminance_reward(
        config.max_luminance, preferences.target_luminance, config)
]


min_luminance_reward = min(luminance_edges)
max_luminance_reward = max(luminance_edges)

print("min luminance reward ", min_luminance_reward)
print("max luminance reward ", max_luminance_reward)

print("normiliazed luminance reward ", strategy.normalize(
    luminance_reward, max_luminance_reward, min_luminance_reward))

normalize_rewards = Normalization()

normalize_rewards.set_strategy(strategy)

new_temp = normalize_rewards.normalize(temp_reward)
new_humidity = normalize_rewards.normalize(humidity_reward)
new_luminance = normalize_rewards.normalize(luminance_reward)

print("temp reward ", temp_reward)
print("normalized temp reward ", new_temp)

print("humidity reward ", humidity_reward)
print("normalized humidity reward ", new_humidity)

print("luminance reward ", luminance_reward)
print("normalized luminance reward ", new_luminance)
"""


current_values = np.linspace(0.1, 30.0, 400)
target_value = 30

rewards = [MathFunctions.temp_reward(temp, target_value, config)
           for temp in current_values]

plt.figure(figsize=(8, 6))
plt.plot(current_values, rewards, label='temp_reward function')
plt.xlabel('Current Temperature')
plt.ylabel('Reward')
plt.title('Plot of temp_reward Function')
plt.legend()
plt.grid(True)
plt.show()
