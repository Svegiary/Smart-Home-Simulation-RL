"""
Calculates sunlight data for a given timestamp
"""
from simulation.config.simulation_config import SimulationConfig


class SunlightCalculation:
    @staticmethod
    def generate_sunlight(index, duration_hours, config: SimulationConfig):

        no_timestamps = duration_hours / (config.time_interval / 60)
        print("STEPS ", no_timestamps)
        if index < no_timestamps // 2:
            sunlight = (index / (no_timestamps // 2))
            print("SUNLIGHT IS ", sunlight)
        else:
            sunlight = 2.0 - (index / (no_timestamps // 2))
            print("SUNLIGHT IS ", sunlight)
        return round(sunlight, 2)
