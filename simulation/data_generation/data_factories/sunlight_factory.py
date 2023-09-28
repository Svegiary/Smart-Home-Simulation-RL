"""
Generates data for the outside temp. The temp will first rise and then fall
saves the data in a dict data[timestamp] = value

"""

from simulation.config.simulation_config import SimulationConfig
from simulation.data_generation.data_calculation.calculate_sunlight import SunlightCalculation
from simulation.data_generation.data_factories.data_factory_interface import DataFactory
from simulation.data_generation.timestamp_generation.timestamp import TimestampGeneration


class SunlightFactory(DataFactory):
    def __init__(self, config: SimulationConfig, timestamps: TimestampGeneration):
        super().__init__(config, timestamps)

    def generateData(self):

        for index, timestamp in enumerate(self.timestamps.timestamps):
            value = SunlightCalculation.generate_sunlight(
                index, self.config.simulation_duration, self.config)
            self.data[timestamp] = value
