import math

from simulation.config.simulation_config import SimulationConfig


class MathFunctions:

    @staticmethod
    def temp_reward(current_temp: float, target_temp: float, config: SimulationConfig):

        if current_temp >= config.min_temp and current_temp <= target_temp:

            return math.log(current_temp - (target_temp - (config.max_temp - config.min_temp)), 2)

        elif current_temp > target_temp and current_temp <= config.max_temp:
            print("current_temp", current_temp)

            return math.log(config.max_temp + (target_temp - config.min_temp) - current_temp, 2)

    @staticmethod
    def humidity_reward(current_humidity: float, target_humidity: float, config: SimulationConfig):

        if current_humidity >= config.min_humidity and current_humidity <= target_humidity:

            return math.log(current_humidity - (target_humidity - (config.max_humidity - config.min_humidity)), 2)

        elif current_humidity > target_humidity and current_humidity <= config.max_humidity:
            print("current_humidity", current_humidity)

            return math.log(config.max_humidity + (target_humidity - config.min_humidity) - current_humidity, 2)

    @staticmethod
    def luminance_reward(current_luminance: float, target_luminance: float, config: SimulationConfig):
        if current_luminance >= config.min_luminance and current_luminance <= target_luminance:

            return math.log(current_luminance - (target_luminance - (config.max_luminance - config.min_luminance)), 2)

        elif current_luminance > target_luminance and current_luminance <= config.max_luminance:
            print("current_luminance", current_luminance)

            return math.log(config.max_luminance + (target_luminance - config.min_luminance) - current_luminance, 2)
