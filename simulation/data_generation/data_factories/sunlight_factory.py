from simulation.config.simulation_config import SimulationConfig
from simulation.data_generation.data_calculation.calculate_sunlight import SunlightCalculation
from simulation.data_generation.data_factories.data_factory_interface import DataFactory
from simulation.data_generation.timestamp_generation.timestamp import TimestampGeneration


class SunlightFactory(DataFactory):
    def __init__(self, config: SimulationConfig, timestamps: TimestampGeneration):
        super().__init__(config, timestamps)

    def generateData(self):
        current_timestamp = self.current_time
        ending_timestamp = self.end_time
        print("THERE ARE ", len(self.timestamps.timestamps))
        for index, timestamp in enumerate(self.timestamps.timestamps):
            current_timestamp = timestamp
            value = SunlightCalculation.generate_sunlight(
                index, current_timestamp, self.config.simulation_duration, self.config)
            self.data[timestamp] = value
