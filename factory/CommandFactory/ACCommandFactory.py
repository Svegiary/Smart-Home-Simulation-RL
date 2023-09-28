from models.devices.ac.ac import AirConditioner
from models.Command.ACCommands import *


class ACCommandFactory:

    def __init__(self, ac: AirConditioner):
        self.ac = ac
        self.commands = []

    def create_commands(self):
        self.commands.append(ACSetCoolingCommand(self.ac))
        self.commands.append(ACSetHeatingCommand(self.ac))
        self.commands.append(ACTurnOffCommand(self.ac))
