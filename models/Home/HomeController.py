from enums.Rooms import HomeRooms
from models.Devices.Device import Device
from enums.DeviceType import DeviceType
from models.Home.Home import Home


class HomeController:

    def __init__(self, home: Home):
        self.home = home

    def turn_on_device(self, room: HomeRooms, device_type: DeviceType):
        self.home[room].devices[device_type].turn_on()

    def turn_off_device(self, room: HomeRooms, device_type: DeviceType):
        self.home[room].devices[device_type].turn_off()
