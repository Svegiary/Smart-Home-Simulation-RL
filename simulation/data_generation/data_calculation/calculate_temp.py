from simulation.config.simulation_config import SimulationConfig
from simulation.data_generation.timestamp_generation.timestamp import TimestampGeneration


class TemperatureCalculation:

    @staticmethod
    def generate_temperature(timestamp, duration_hours, config: SimulationConfig):
        half_duration = duration_hours // 2
        current_hour = (timestamp % 86400) / 3600

        if current_hour < half_duration:
            temperature = config.max_temp - \
                (current_hour / half_duration) * \
                (config.max_temp - config.min_temp)
        else:
            temperature = config.min_temp + \
                ((current_hour - half_duration) / half_duration) * \
                (config.max_temp - config.min_temp)

        return round(temperature, 1)
