"""
Singleton class for generating timestamps
"""

import time
from simulation.config.simulation_config import SimulationConfig


class TimestampGeneration:
    _instance = None

    def __new__(cls, config: SimulationConfig):
        if cls._instance is None:
            cls._instance = super(TimestampGeneration, cls).__new__(cls)
            cls._instance.initialize(config)
        return cls._instance

    def initialize(self, config: SimulationConfig):
        self.config = config
        self.current_time: int = int(time.time())
        self.end_time: int = self.current_time + config.simulation_duration * 3600
        self.timestamps: list[int] = []

    def generate_timestamps(self):
        starting_time = self.current_time
        end_time = self.end_time
        while starting_time < end_time:
            self.timestamps.append(starting_time)
            starting_time += self.config.time_interval * 60

    def timestamp_iterator(self):
        for timestamp in self.timestamps:
            yield timestamp
