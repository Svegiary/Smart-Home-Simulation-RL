from simulation.config.simulation_config import SimulationConfig


class HumidityCalculation:

    @staticmethod
    def generate_humidity(index: int, duration_hours: float, config: SimulationConfig) -> float:
        """
        Generates a humidity value based on the index of the timestamp.

        Args:
            index (int): Index of the timestamp.
            duration_hours (float): Duration of the simulation in hours.
            config (SimulationConfig): Configuration of the simulation.

        Returns:
            float: Humidity value.
        """
        # Calculate the total number of timestamps in the simulation.
        no_timestamps = duration_hours / (config.time_interval / 60)

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
