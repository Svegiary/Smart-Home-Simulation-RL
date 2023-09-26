from abc import abstractmethod, ABC
from time import sleep
from enums.Rooms import HomeRooms
from models.Command.Invoker import Invoker

from simulation.SimulationSnapshot import SimulationSnapshot


class SimulationRuntime(ABC):
    def __init__(self):
        self.snapshots: list[SimulationSnapshot] = []
        self.invoker = Invoker()  # TODO: hell no

    @abstractmethod
    def start(self, sim):
        pass


class NoRuntime(SimulationRuntime):
    def start(self, sim):
        print("Please set runtime plan")


class DefaultRuntime(SimulationRuntime):
    def start(self, sim):
        for timestamp in sim.timestamps:
            snapshot = sim.extract_snapshot(timestamp)
            self.snapshots.append(snapshot)
            snapshot.print()
            sleep(0.1)


class CallToActionRuntime(SimulationRuntime):
    def start(self, sim):
        for timestamp in sim.timestamps:
            snapshot = sim.extract_snapshot(timestamp)
            self.snapshots.append(snapshot)
            snapshot.print()
            execute = input("Choose Action")
            sleep(0.1)


class ControllerAcRuntime(SimulationRuntime):
    def start(self, sim):
        for timestamp in sim.timestamps:
            snapshot = sim.extract_snapshot(timestamp)
            self.snapshots.append(snapshot)
            snapshot.print()
            print("Actions")
            print("1) Set cooling")
            print("2) Set Heating")
            print("3) Turn off")
            print("4) Do nothing")
            while True:
                command = input("Option:")
                if command == "1":

                    sim.controller.set_cooling()
                    break
                elif command == "2":

                    sim.controller.set_heating()
                    break
                elif command == "3":
                    sim.controller.turn_off_ac()
                    break
                elif command == "4":
                    print("doing nothing")
                    break
                else:
                    print("invalid action")
                    continue
            print("------------------------------------")


class ControllerDehumidifierRuntime(SimulationRuntime):
    def start(self, sim):
        for timestamp in sim.timestamps:
            snapshot = sim.extract_snapshot(timestamp)
            self.snapshots.append(snapshot)
            snapshot.print()
            print("Actions")
            print("1) Turn off")
            print("2) Turn on")
            print("3) Do nothing")
            while True:
                command = input("Option:")
                if command == "1":

                    sim.controller.turn_off_dehumidifier()
                    break
                elif command == "2":

                    sim.controller.turn_on_dehumidifier()
                    break
                elif command == "3":
                    break

                else:
                    print("invalid action")
                    continue
            print("------------------------------------")


class HumanMovementRuntime(SimulationRuntime):
    def start(self, sim):
        for timestamp in sim.timestamps:
            snapshot = sim.extract_snapshot(timestamp)
            self.snapshots.append(snapshot)
            snapshot.print()
            print("Actions")
            print("1) Move human to living room")
            print("2) Move human to bedroom")
            print("3) Move human to bathroom")
            print("4) Move human to kitchen")
            print("5) Dont move")
            while True:
                command = input("Option:")
                if command == "1":

                    sim.home.place_human(HomeRooms.LIVING_ROOM)
                    break
                elif command == "2":

                    sim.home.place_human(HomeRooms.BEDROOM)
                    break
                elif command == "3":
                    sim.home.place_human(HomeRooms.BATHROOM)
                    break
                elif command == "4":
                    sim.home.place_human(HomeRooms.KITCHEN)
                    break
                elif command == "5":
                    break
                else:
                    print("invalid action")
                    continue
            print("------------------------------------")
