"""
This file contains logic for extracting the new snapshot
of the simulation taking into account changes by the environment
and the devices
"""

from enums.Rooms import HomeRooms
from simulation.SnapshotDataCalculator import SnapshotDataCalculator
from simulation.data_generation.simulation_data import SimulationData
from simulation.human.human import Human
from colorama import Fore, Back, Style
from termcolor import colored


class SimulationSnapshot:
    """
    Create a new Simulation based on current external variables
    and the devices
    """

    def __init__(self,
                 simulation_data: SimulationData,
                 human:  Human,
                 calculator: SnapshotDataCalculator):
        # avoiding circular imports
        from simulation.power_calculator.power_calculator import PowerCalculator

        self.outside_temp: float = simulation_data["temp"]
        self.outside_humidity: float = simulation_data["humidity"]
        self.sunlight: float = simulation_data["sunlight"]
        self.inside_temp = calculator.calculate_temp(
            simulation_data["temp"])  # calculate new inside temp
        self.inside_humidity = calculator.calculate_humidity(
            simulation_data["humidity"])  # calculate new inside humidity
        self.luminances = calculator.calculate_luminance(
            simulation_data["sunlight"])
        self.human_location = human.human_location  # get human location
        self.current_power = PowerCalculator.calculate_power(
            calculator.home_device_snapshot)
        self

    def print(self):
        """
        Prints the current simulation snapshot
        """
        print(Fore.BLACK, Back.CYAN,
              '/////////////////////////////////////////////////////////////////', Back.BLACK)
        print("")
        print(Fore.BLACK, Back.WHITE, "Outside temp : ", Back.BLACK, Fore.WHITE, self.outside_temp,
              Fore.BLACK,  Back.WHITE, "| Inside temp : ", Back.BLACK, Fore.WHITE, self.inside_temp)
        print(Fore.RED, "------------------------------------------------------------")
        print(Fore.BLACK, Back.WHITE, "Outside humidity : ", Back.BLACK, Fore.WHITE, self.outside_humidity,
              Fore.BLACK,  Back.WHITE, "| Inside humidity : ", Back.BLACK, Fore.WHITE, self.inside_humidity)
        print(Fore.RED, "------------------------------------------------------------")
        print(Fore.BLACK, Back.WHITE, "Living Room Luminance: ",
              Back.BLACK, Fore.WHITE, self.luminances[HomeRooms.LIVING_ROOM],
              Fore.BLACK, Back.WHITE, "Bed Room Luminance: ",
              Back.BLACK, Fore.WHITE, self.luminances[HomeRooms.BEDROOM]
              )
        print(Back.BLACK, "")
        print(Fore.BLACK, Back.WHITE, "Kitchen Luminance: ",
              Back.BLACK, Fore.WHITE, self.luminances[HomeRooms.KITCHEN],
              Fore.BLACK, Back.WHITE, "Bathroom Luminance: ",
              Back.BLACK, Fore.WHITE, self.luminances[HomeRooms.BEDROOM]
              )
        print(Fore.RED, "------------------------------------------------------------")
        print(Fore.BLACK, Back.WHITE, "Human location : ", Back.BLACK, Fore.WHITE,
              self.human_location.name)
        print(Fore.RED, "-----------------------------------------------")
        print(Fore.BLACK, Back.RED,
              "Snapshot Energy Consumption : ", Back.BLACK, Fore.WHITE, self.current_power)
        print("")
        print(Fore.BLACK, Back.CYAN,
              '/////////////////////////////////////////////////////////////////', Back.BLACK, Fore.WHITE)
