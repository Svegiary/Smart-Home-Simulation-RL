from simulation.config.simulation_config import SimulationConfig
from simulation.data_generation.data_calculation.calculate_humidity import HumidityCalculation
from simulation.data_generation.data_factories.data_factory_interface import DataFactory
from simulation.data_generation.timestamp_generation.timestamp import TimestampGeneration


class HumidityFactory(DataFactory):
    def __init__(self, config: SimulationConfig, timestamps: TimestampGeneration):
        super().__init__(config, timestamps)

    def generateData(self):

        for index, timestamp in enumerate(self.timestamps.timestamps):
            value = HumidityCalculation.generate_humidity(
                index, self.config.simulation_duration, self.config)
            self.data[timestamp] = value
