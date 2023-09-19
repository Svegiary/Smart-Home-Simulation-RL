from simulation.data_generation.simulation_data import SimulationData
from simulation.data_generation.timestamp_generation.timestamp import TimestampGeneration


class Simulation:
    def __init__(self, timestamps: TimestampGeneration, simulation_data: SimulationData,):
        self.timestamps = timestamps.timestamps
        self.simulation_data = simulation_data
