from models.command.ac_commands import *
from models.command.dehumidifier_commands import TurnOffDehumidifier, TurnOnDehumidifier
from models.command.device_command import DeviceCommand
from models.command.invoker import Invoker


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
