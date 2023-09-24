from models.Home.Home import Home
from simulation.HomeTempCalculator import HomeTempCalculator
from simulation.SimulationController import SimulationController
from simulation.data_generation.simulation_data import SimulationData
from simulation.data_generation.timestamp_generation.timestamp import TimestampGeneration
from simulation.SimulationRuntime import *
from simulation.device_influence.DeviceInfluence import DeviceInfluence


class Simulation:
    def __init__(
            self,
            timestamps: TimestampGeneration,
            simulation_data:  SimulationData,
            home: Home,
            controller: SimulationController
    ):
        self.timestamps = timestamps.timestamps
        self.simulation_data = simulation_data
        self.home = home
        self.simulation_runtime_plan = NoRuntime()
        self.simulation_controller = 0

    def set_runtime_plan(self, runtime_plan: SimulationRuntime):
        self.simulation_runtime_plan = runtime_plan

    def start(self):
        self.simulation_runtime_plan.start(self)

    def extract_snapshot(self, timestamp):

        return SimulationSnapshot(
            self.home.house_temp,
            self.simulation_data.temp_data[timestamp],
            HomeTempCalculator(DeviceInfluence(self.home))

        )


# simulation has states .
# evaluation based on preferences


class SnapshotGeneration:
    def __init__(self, device_influence):
        pass

    def calculate_temp(self, sim: Simulation):
        pass
