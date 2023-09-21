from simulation.config.simulation_config import SimulationConfig
from simulation.data_generation.data_calculation.calculate_humidity import HumidityCalculation
from simulation.data_generation.data_factories.data_factory_interface import DataFactory
from simulation.data_generation.timestamp_generation.timestamp import TimestampGeneration


class HumidityFactory(DataFactory):
    def __init__(self, config: SimulationConfig, timestamps: TimestampGeneration):
        super().__init__(config, timestamps)
        self.data = {}

    def generateData(self):

        starting_timestamp = self.current_time
        ending_timestamp = self.end_time
        while starting_timestamp < ending_timestamp:
            timestamp = starting_timestamp
            value = HumidityCalculation.generate_humidity(
                starting_timestamp, self.config.simulation_duration, self.config)
            self.data[timestamp] = value
            starting_timestamp += self.config.time_interval * 60
