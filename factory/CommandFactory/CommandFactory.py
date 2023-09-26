from enums.DeviceType import DeviceType
from factory.CommandFactory.ACCommandFactory import ACCommandFactory
from factory.CommandFactory.DehumidifierCommandFactory import DehumidifierCommandFactory
from factory.CommandFactory.LightBulbCommandFactory import LightBulbCommandFactory
from models.Command.DeviceCommand import DeviceCommand
from models.Home.Home import Home


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
