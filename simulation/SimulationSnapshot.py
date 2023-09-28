"""
This file contains logic for extracting the new snapshot
of the simulation taking into account changes by the environment
and the devices
"""

from simulation.SnapshotDataCalculator import SnapshotDataCalculator
from simulation.human.human import Human


class SimulationSnapshot:
    def __init__(self, outside_temp: float, outside_humidity: float, human:  Human, calculator: SnapshotDataCalculator):
        self.outside_temp = outside_temp
        self.outside_humidity = outside_humidity
        self.inside_temp = calculator.calculate_temp(
            outside_temp)  # calculate new inside temp
        self.inside_humidity = calculator.calculate_humidity(
            outside_humidity)  # calculate new inside humidity

        self.human_location = human.human_location  # get human location

    def print(self):
        print("//////////////////////////////////////////////")
        print("Outside temp : ", self.outside_temp,
              "| Inside temp : ", self.inside_temp)
        print("-----------------------------------------------")
        print("Outside humidity : ", self.outside_humidity,
              "| Inside humidity : ", self.inside_humidity)
        print("-----------------------------------------------")
        print("Human location : ", self.human_location.name)
        print("-----------------------------------------------")
