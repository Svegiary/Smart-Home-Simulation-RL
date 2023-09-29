"""
Centralized command factory for creating all available commands
for each device in the house. 
"""

from enums.DeviceType import DeviceType
from factory.command_factory.ac_command_factory import ACCommandFactory
from factory.command_factory.dehumidifier_command_factory import DehumidifierCommandFactory
from factory.command_factory.light_bulb_command_factory import LightBulbCommandFactory
from models.command.device_command import DeviceCommand
from models.home.home import Home


class CommandFactory:
    """
    Centralized command factory for creating all available commands
    for each device in the house. 
    """

    @staticmethod
    def create_commands(home: Home) -> tuple[DeviceCommand]:
        """
        Creating commands for all devices. Returns a tuple
        """
        commands = []
        for room in home.rooms.values():
            for device_type, device in room.devices.items():
                if device_type == DeviceType.AC:
                    commands += ACCommandFactory.create_commands(device)

                if device_type == DeviceType.LIGHT:

                    commands += LightBulbCommandFactory.create_commands(device)
                if device_type == DeviceType.DEHUMIDIFIER:
                    commands += DehumidifierCommandFactory.create_commands(
                        device)
        return tuple(commands)
