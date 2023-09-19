from models.Home.Home import Home
from models.Home.HomeController import HomeController
from simulation.data_generation.simulation_data import SimulationData
from simulation.data_generation.timestamp_generation.timestamp import TimestampGeneration


class Simulation:
    def __init__(
            self, timestamps: TimestampGeneration,
            simulation_data: SimulationData,
            home: Home,
            homeController: HomeController,
    ):
        self.timestamps = timestamps.timestamps
        self.simulation_data = simulation_data
        self.home = home


# simulation has states .
# evaluation based on preferences
