"""
Calculates sunlight data for a given timestamp
"""
from simulation.config.simulation_config import SimulationConfig


class SunlightCalculation:
    @staticmethod
    def generate_sunlight(index, config: SimulationConfig):
        """
        Generates sunlight value for a give timestamp
        """

        no_timestamps = config.simulation_duration / \
            (config.time_interval / 60)
        if index < no_timestamps // 2:
            sunlight = (index / (no_timestamps // 2))
        else:
            sunlight = 2.0 - (index / (no_timestamps // 2))
        return round(sunlight, 2)
