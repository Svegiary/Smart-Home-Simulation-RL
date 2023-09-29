"""
Calculates temp data fo a given timestamp
"""
from simulation.config.simulation_config import SimulationConfig


class TemperatureCalculation:

    @staticmethod
    def generate_temperature(index: int,  config: SimulationConfig) -> float:
        """
        Generates temp value for a give timestamp
        """

        # Calculate the total number of timestamps in the simulation.
        no_timestamps = config.simulation_duration / \
            (config.time_interval / 60)

        if index < no_timestamps / 2:
            # In the first half, temperature rises from min_temp to max_temp linearly.
            temperature = config.min_temp + \
                (index / (no_timestamps / 2)) * \
                (config.max_temp - config.min_temp)
        else:
            # In the second half, temperature decreases from max_temp to min_temp linearly.
            temperature = config.max_temp - \
                ((index - (no_timestamps / 2)) / (no_timestamps / 2)) * \
                (config.max_temp - config.min_temp)

        return round(temperature, 1)
