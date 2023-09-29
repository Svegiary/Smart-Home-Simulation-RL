

from models.home.home import Home
from simulation.SimulationRuntime import NoRuntime, SimulationRuntime
from simulation.SimulationSnapshot import SimulationSnapshot
from simulation.SnapshotDataCalculator import SnapshotDataCalculator
from simulation.SimulationController import SimulationController
from simulation.config.simulation_config import SimulationConfig
from simulation.data_generation.simulation_data import SimulationData
from simulation.data_generation.timestamp_generation.timestamp import TimestampGeneration
from simulation.home_devices_snapshot.home_device_snapshot import HomeDeviceSnapshot


class Simulation:
    """

    This class is responsible for creating the simulation 
    Its' responsbilities:
        1) start the simulation
        2) set a runtime plan (No action , choose action , choose ac action etc)
        3) extract a simulation snapshot based on the current state of the simulation

    """

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

    def set_runtime_plan(self, runtime_plan: SimulationRuntime) -> None:
        """
        Method to set the runtime plan for the simulation
        """

        self.simulation_runtime_plan = runtime_plan

    def start(self) -> None:
        """
        Method to start the simulation
        """
        self.simulation_runtime_plan.start(self)

    #
    def extract_snapshot(self, timestamp: int) -> SimulationSnapshot:
        """
        Method to extract a simulation snapshot at a given timestamp
        """
        return SimulationSnapshot(
            self.simulation_data.get_data_for_timestamp(timestamp),
            self.home.human,
            SnapshotDataCalculator(HomeDeviceSnapshot(self.home))
        )
