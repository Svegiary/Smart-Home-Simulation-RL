from enums.DeviceType import DeviceType
from models.devices.device import Device
from models.devices.light_bulb.light_bulb_state import OnState
from rl_env.math_functions import MathFunctions
from rl_env.reward_normalization.normalization_strategy import MinMaxNormalization
from simulation.SimulationSnapshot import SimulationSnapshot
from simulation.config.simulation_config import SimulationConfig
from simulation.power_calculator.power_calculator import PowerCalculator
from simulation.preferences.simulation_preferences import Preferences


class RewardCalculation:

    def __init__(self, snapshot: SimulationSnapshot, preferences: Preferences, config: SimulationConfig):
        self.snapshot = snapshot
        self.preferences = preferences
        self.config = config

    def temp_reward(self):
        reward = MathFunctions.temp_reward(self.snapshot.inside_temp,
                                           self.preferences.target_temp,
                                           self.config,
                                           )
        temp_edges = [MathFunctions.temp_reward(self.config.min_temp, self.preferences.target_temp, self.config),
                      MathFunctions.temp_reward(
                          self.config.max_temp, self.preferences.target_temp, self.config),
                      MathFunctions.temp_reward(self.preferences.target_temp, self.preferences.target_temp, self.config)]
        min_temp_reward = min(temp_edges)
        max_temp_reward = max(temp_edges)
        normalization = MinMaxNormalization()
        return normalization.normalize(reward, max_temp_reward, min_temp_reward)

    def luminance_reward(self):
        human_location = self.snapshot.human_location
        luminance = self.snapshot.luminances[human_location.name]
        reward = MathFunctions.luminance_reward(luminance,
                                                self.preferences.target_luminance,
                                                self.config,
                                                )
        luminance_edges = [MathFunctions.luminance_reward(self.config.min_luminance, self.preferences.target_luminance, self.config),
                           MathFunctions.luminance_reward(
                               self.config.max_luminance, self.preferences.target_luminance, self.config),
                           MathFunctions.luminance_reward(self.preferences.target_luminance, self.preferences.target_luminance, self.config)]

        min_luminance_reward = min(luminance_edges)
        max_luminance_reward = max(luminance_edges)
        normalization = MinMaxNormalization()
        return normalization.normalize(reward, max_luminance_reward, min_luminance_reward)

    def humidity_reward(self):
        reward = MathFunctions.humidity_reward(self.snapshot.humidity,
                                               self.preferences.target_humidity,
                                               self.config,
                                               )
        humidity_edges = [MathFunctions.humidity_reward(self.config.min_humidity, self.preferences.target_humidity, self.config),
                          MathFunctions.humidity_reward(
                              self.config.max_humidity, self.preferences.target_humidity, self.config),
                          MathFunctions.humidity_reward(self.preferences.target_humidity, self.preferences.target_humidity, self.config)]
        min_humidity_reward = min(humidity_edges)
        max_humidity_reward = max(humidity_edges)
        normalization = MinMaxNormalization()
        return normalization.normalize(reward, max_humidity_reward, min_humidity_reward)

    def power_reward(self, devices: list[Device]):
        max_energy: float = PowerCalculator.theoretical_max_evergy(devices)
        min_energy = 0.0
        normalization = MinMaxNormalization()
        return normalization.normalize(self.snapshot.current_power, max_energy, min_energy)
