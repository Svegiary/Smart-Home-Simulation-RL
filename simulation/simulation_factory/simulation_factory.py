from simulation.Simulation import Simulation
from simulation.config.simulation_config import SimulationConfig
from simulation.data_generation.data_factories.temperature_factory import TemperatureFactory
from simulation.data_generation.simulation_data import SimulationData
from simulation.data_generation.simulation_data_factory import SimulationDataFactory
from simulation.data_generation.timestamp_generation.timestamp import TimestampGeneration


class SimulationFactory:

    def __init__(self, config: SimulationConfig):
        self.config = config

    def create_simulation(self):
        timestamps = TimestampGeneration(self.config)
        temp = TemperatureFactory(self.config, timestamps)
        data = SimulationDataFactory.create_simulation_data(temp, 0, 0)
        return Simulation(timestamps, data)
