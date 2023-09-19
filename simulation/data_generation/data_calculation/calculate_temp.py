from simulation.config.simulation_config import SimulationConfig
from simulation.data_generation.timestamp_generation.timestamp import TimestampGeneration


class TemperatureCalculation:

    @staticmethod
    def generate_temperature(timestamp, duration_hours, config: SimulationConfig):
        # Simulate a temperature pattern over 24 hours (decreasing and then increasing)
        half_duration = duration_hours // 2
        # Calculate the current hour in the day
        current_hour = (timestamp % 86400) / 3600

        if current_hour < half_duration:
            # In the first half of the day, decrease temperature
            temperature = config.max_temp - \
                (current_hour / half_duration) * \
                (config.max_temp - config.min_temp)
        else:
            # In the second half, increase temperature
            temperature = config.min_temp + \
                ((current_hour - half_duration) / half_duration) * \
                (config.max_temp - config.min_temp)

        return round(temperature, 1)
