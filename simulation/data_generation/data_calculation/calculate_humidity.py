"""
Generates a humidity value based on the index of the timestamp.

"""

from simulation.config.simulation_config import SimulationConfig


class HumidityCalculation:

    @staticmethod
    def generate_humidity(index: int, config: SimulationConfig) -> float:
        """
        Generates humidity value for a give timestamp
        """

        # Calculate the total number of timestamps in the simulation.
        no_timestamps = config.simulation_duration / \
            (config.time_interval / 60)

        if index < no_timestamps / 2:
            # In the first half, humidity rises from min_humidity to max_humidity linearly.
            humidity = config.min_humidity + \
                (index / (no_timestamps / 2)) * \
                (config.max_humidity - config.min_humidity)
        else:
            # In the second half, humidity decreases from max_humidity to min_humidity linearly.
            humidity = config.max_humidity - \
                ((index - (no_timestamps / 2)) / (no_timestamps / 2)) * \
                (config.max_humidity - config.min_humidity)

        return round(humidity, 1)
