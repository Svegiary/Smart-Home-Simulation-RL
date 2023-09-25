from models.Command.ACCommands import *
from models.Command.DeviceCommand import DeviceCommand
from models.Command.Invoker import Invoker
from simulation.device_influence.DeviceInfluence import DeviceInfluence


class SimulationController:
    def __init__(self, commands: list[DeviceCommand], invoker: Invoker):
        self.commands = commands
        self.invoker = invoker

    def set_heating(self):
        for command in self.commands:
            if isinstance(command, ACSetHeatingCommand):
                self.execute(command)

    def set_cooling(self):
        for command in self.commands:
            if isinstance(command, ACSetCoolingCommand):
                self.execute(command)

    def turn_off(self):
        for command in self.commands:
            if isinstance(command, ACTurnOffCommand):
                self.execute(command)

    def execute(self, command):
        self.invoker.execute(command)
