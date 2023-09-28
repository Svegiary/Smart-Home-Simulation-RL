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


class CommandFactory():
    def __init__(self, home: Home):
        self.home = home
        self.commands: list[DeviceCommand] = []

    def create_commands(self):
        for room in self.home.rooms.values():
            for device_type, device in room.devices.items():
                if device_type == DeviceType.AC:
                    ac_factory = ACCommandFactory(device)
                    ac_factory.create_commands()
                    self.commands += ac_factory.commands
                if device_type == DeviceType.LIGHT:
                    light_factory = LightBulbCommandFactory(device)
                    light_factory.create_commands()
                    self.commands += light_factory.commands
                if device_type == DeviceType.DEHUMIDIFIER:
                    dehumidifier_factory = DehumidifierCommandFactory(device)
                    dehumidifier_factory.create_commands()
                    self.commands += dehumidifier_factory.commands
