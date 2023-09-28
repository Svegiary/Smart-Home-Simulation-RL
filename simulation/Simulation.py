"""
-Simulation.py
This class is responsible for creating the simulation 
Its' responsbilities:
    1) start the simulation
    2) set a runtime plan (No action , choose action , choose ac action etc)
    3) extract a simulation snapshot based on the current state of the simulation

"""


from models.home.home import Home
from simulation.SnapshotDataCalculator import SnapshotDataCalculator
from simulation.SimulationController import SimulationController
from simulation.config.simulation_config import SimulationConfig
from simulation.data_generation.simulation_data import SimulationData
from simulation.data_generation.timestamp_generation.timestamp import TimestampGeneration
from simulation.SimulationRuntime import *
from simulation.home_devices_snapshot.home_device_snapshot import HomeDeviceSnapshot


class Simulation:
    def __init__(
            self,
            timestamps_generator: TimestampGeneration,
            simulation_data:  SimulationData,
            home: Home,
            controller: SimulationController,
            config: SimulationConfig,
    ) -> None:
        # Initialize instance variables with simulation-related data
        self.timestamps = timestamps_generator.timestamps
        self.simulation_data = simulation_data
        self.home = home
        self.simulation_runtime_plan = NoRuntime()  # Default to NoRuntime
        self.controller = controller  # temporary controller for excecuting actions
        self.config = config

    # Method to set the runtime plan for the simulation
    def set_runtime_plan(self, runtime_plan: SimulationRuntime) -> None:
        self.simulation_runtime_plan = runtime_plan

    # Method to start the simulation
    def start(self) -> None:
        self.simulation_runtime_plan.start(self)

    # Method to extract a simulation snapshot at a given timestamp
    def extract_snapshot(self, timestamp) -> SimulationSnapshot:
        return SimulationSnapshot(
            self.simulation_data.temp_data[timestamp],
            self.simulation_data.humidity_data[timestamp],
            self.home.human,
            SnapshotDataCalculator(HomeDeviceSnapshot(self.home))
        )
