from simulation.config.simulation_config import SimulationConfig


class TemperatureCalculation:

    @staticmethod
    def generate_temperature(index: int, duration_hours: int, config: SimulationConfig) -> float:
        """
        Generates a temperature value based on the index of the timestamp.

        Args:
            index (int): Index of the timestamp.
            duration_hours (int): Duration of the simulation in hours.
            config (SimulationConfig): Configuration of the simulation.

        Returns:
            float: Temperature value.
        """
        # Calculate the total number of timestamps in the simulation.
        no_timestamps = duration_hours / (config.time_interval / 60)

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
