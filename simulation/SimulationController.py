from factory.CommandFactory.DehumidifierCommandFactory import DehumidifierCommandFactory
from models.Command.ACCommands import *
from models.Command.DehumidifierCommands import TurnOffDehumidifier, TurnOnDehumidifier
from models.Command.DeviceCommand import DeviceCommand
from models.Command.Invoker import Invoker


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

    def turn_off_ac(self):
        for command in self.commands:
            if isinstance(command, ACTurnOffCommand):
                self.execute(command)

    def turn_on_dehumidifier(self):
        for command in self.commands:
            if isinstance(command, TurnOnDehumidifier):
                self.execute(command)

    def turn_off_dehumidifier(self):
        for command in self.commands:
            if isinstance(command, TurnOffDehumidifier):
                self.execute(command)

    def execute(self, command):
        self.invoker.execute(command)
