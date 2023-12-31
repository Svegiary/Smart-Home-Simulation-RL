

from abc import ABC, abstractmethod

from simulation.config.simulation_config import SimulationConfig
from simulation.data_generation.timestamp_generation.timestamp import TimestampGeneration


class DataFactory(ABC):
    def __init__(self, config: SimulationConfig, timestamps: TimestampGeneration):
        self.config = config
        self.timestamps = timestamps
        self.data = {}

    @abstractmethod
    def generateData(self):
        pass
