from enums.DeviceType import DeviceType
from enums.Rooms import HomeRooms
from models.command.ac_commands import *
from models.command.dehumidifier_commands import TurnOffDehumidifier, TurnOnDehumidifier
from models.command.device_command import DeviceCommand
from models.command.invoker import Invoker
from models.home.home import Home


class SimulationController:
    def __init__(self, commands: list[DeviceCommand], invoker: Invoker, home: Home):
        self.commands = commands
        self.invoker = invoker
        self.home = home

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

    def open_kitchen_light(self):
        self.home.rooms[HomeRooms.KITCHEN].devices[DeviceType.LIGHT].turn_on()

    def open_living_room_light(self):
        self.home.rooms[HomeRooms.LIVING_ROOM].devices[DeviceType.LIGHT].turn_on()

    def open_bedroom_light(self):
        self.home.rooms[HomeRooms.BEDROOM].devices[DeviceType.LIGHT].turn_on()

    def open_bathroom_light(self):
        self.home.rooms[HomeRooms.BATHROOM].devices[DeviceType.LIGHT].turn_on()

    def close_kitchen_light(self):
        self.home.rooms[HomeRooms.KITCHEN].devices[DeviceType.LIGHT].turn_off()

    def close_living_room_light(self):
        self.home.rooms[HomeRooms.LIVING_ROOM].devices[DeviceType.LIGHT].turn_off()

    def close_bedroom_light(self):
        self.home.rooms[HomeRooms.BEDROOM].devices[DeviceType.LIGHT].turn_off()

    def close_bathroom_light(self):
        self.home.rooms[HomeRooms.BATHROOM].devices[DeviceType.LIGHT].turn_off()

    def togle_light(self, room: HomeRooms):
        if self.home.rooms[room].devices[DeviceType.LIGHT].state._brightness == 0:
            self.home.rooms[room].devices[DeviceType.LIGHT].turn_on()
        else:
            self.home.rooms[room].devices[DeviceType.LIGHT].turn_off()

    def set_light_brightness(self, room: HomeRooms, brightness: int):
        self.home.rooms[room].devices[DeviceType.LIGHT].set_brightness(
            brightness)
