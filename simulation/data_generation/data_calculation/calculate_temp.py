from simulation.config.simulation_config import SimulationConfig
from simulation.data_generation.timestamp_generation.timestamp import TimestampGeneration


class TemperatureCalculation:

    @staticmethod
    def generate_temperature(index, duration_hours, config: SimulationConfig):
        """
        Generates a temperature value based on the index of the timestamp
        :param index: index of the timestamp
        :param timestamp: timestamp of the timestamp
        :param duration_hours: duration of the simulation in hours
        :param config: configuration of the simulation
        :return: temperature value
        """
        no_timestamps = duration_hours / (config.time_interval / 60)

        if index < no_timestamps // 2:

            temperature = config.min_temp + \
                ((index / (no_timestamps // 2)) *
                 (config.max_temp - config.min_temp))
        else:
            temperature = config.max_temp - \
                (((index / (no_timestamps))) *
                 (config.max_temp - config.min_temp))

        return round(temperature, 1)
