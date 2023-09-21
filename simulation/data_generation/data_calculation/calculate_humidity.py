from simulation.config.simulation_config import SimulationConfig


class HumidityCalculation:

    @staticmethod
    def generate_humidity(timestamp, duration_hours, config: SimulationConfig):
        # Simulate a humidity pattern over 24 hours (decreasing and then increasing)
        half_duration = duration_hours // 2
        # Calculate the current hour in the day
        current_hour = (timestamp % 86400) / 3600

        if current_hour < half_duration:
            # In the first half of the day, decrease humidity
            humidity = config.max_humidity - \
                (current_hour / half_duration) * \
                (config.max_humidity - config.min_humidity)
        else:
            # In the second half, increase humidity
            humidity = config.min_humidity + \
                ((current_hour - half_duration) / half_duration) * \
                (config.max_humidity - config.min_humidity)

        return round(humidity, 1)
