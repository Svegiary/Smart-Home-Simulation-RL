"""
Simple factory for creating AC Commands
"""


from models.devices.ac.ac import AirConditioner
from models.command.ac_commands import *


class ACCommandFactory:

    @staticmethod
    def create_commands(ac: AirConditioner) -> list[DeviceCommand]:
        commands = []
        commands.append(ACSetCoolingCommand(ac))
        commands.append(ACSetHeatingCommand(ac))
        commands.append(ACTurnOffCommand(ac))
        return commands
