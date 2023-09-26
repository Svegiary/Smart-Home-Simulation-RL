from simulation.config.simulation_config import SimulationConfig


class HumidityCalculation:

    @staticmethod
    def generate_humidity(index, duration_hours, config: SimulationConfig):

        no_timestamps = duration_hours / (config.time_interval / 60)

        if index < no_timestamps // 2:

            humidity = config.min_humidity + \
                ((index / (no_timestamps // 2)) *
                 (config.max_humidity - config.min_humidity))
        else:
            humidity = config.max_humidity - \
                (((index / (no_timestamps))) *
                 (config.max_humidity - config.min_humidity))

        return round(humidity, 1)
