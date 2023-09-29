"""
Simple factory to create commands for the dehumidifier.
"""

from models.command.dehumidifier_commands import TurnOffDehumidifier, TurnOnDehumidifier
from models.command.device_command import DeviceCommand
from models.devices.dehumidifier.dehumidifier import Dehumidifier


class DehumidifierCommandFactory:

    @staticmethod
    def create_commands(dehumidifier: Dehumidifier) -> list[DeviceCommand]:
        commands = []
        commands.append(TurnOnDehumidifier(dehumidifier))
        commands.append(TurnOffDehumidifier(dehumidifier))
        return commands
