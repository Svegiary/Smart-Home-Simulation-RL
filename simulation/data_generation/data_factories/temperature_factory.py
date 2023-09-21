
from simulation.config.simulation_config import SimulationConfig
from simulation.data_generation.data_calculation.calculate_temp import TemperatureCalculation
from simulation.data_generation.data_factories.data_factory_interface import DataFactory
from simulation.data_generation.timestamp_generation.timestamp import TimestampGeneration


class TemperatureFactory(DataFactory):
    def __init__(self, config: SimulationConfig, timestamps: TimestampGeneration):
        super().__init__(config, timestamps)

    def generateData(self):

        starting_timestamp = self.current_time
        ending_timestamp = self.end_time
        while starting_timestamp < ending_timestamp:
            timestamp = starting_timestamp
            value = TemperatureCalculation.generate_temperature(
                starting_timestamp, self.config.simulation_duration, self.config)
            self.data[timestamp] = value
            starting_timestamp += self.config.time_interval * 60
