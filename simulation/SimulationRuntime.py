from abc import abstractmethod, ABC
from time import sleep

from simulation.SimulationSnapshot import SimulationSnapshot


class SimulationRuntime(ABC):
    def __init__(self):
        self.snapshots: list[SimulationSnapshot] = []

    @abstractmethod
    def start(self, sim):
        pass


class NoRuntime(SimulationRuntime):
    def start(self, sim):
        print("Please set runtime plan")


class DefaultRuntime(SimulationRuntime):
    def start(self, sim):
        for timestamp in sim.timestamps:
            print(timestamp)
            sleep(0.1)


class CallToActionRuntime(SimulationRuntime):
    def start(self, sim):
        for timestamp in sim.timestamps:
            print(timestamp)
            print(sim.simulation_data.temp_data)
            snapshot = sim.extract_snapshot(timestamp)
            self.snapshots.append(snapshot)
            print(vars(snapshot))
            execute = input("Choose Action")
            sleep(0.1)
