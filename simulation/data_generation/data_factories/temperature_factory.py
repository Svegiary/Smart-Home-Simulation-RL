
from simulation.config.simulation_config import SimulationConfig
from simulation.data_generation.data_calculation.calculate_temp import TemperatureCalculation
from simulation.data_generation.timestamp_generation.timestamp import TimestampGeneration


class TemperatureFactory:
    def __init__(self, config: SimulationConfig, timestamps: TimestampGeneration):
        self.config = config

        self.current_time = timestamps.current_time
        self.end_time = timestamps.end_time
        self.data = {}

    def generateTempData(self):

        starting_timestamp = self.current_time
        ending_timestamp = self.end_time
        while starting_timestamp < ending_timestamp:
            timestamp = starting_timestamp
            value = TemperatureCalculation.generate_temperature(
                starting_timestamp, self.config.simulation_duration, self.config)
            self.data[timestamp] = value
            starting_timestamp += self.config.time_interval * 60
