from enums.Rooms import HomeRooms
from models.Devices.Device import Device
from enums.DeviceType import DeviceType
from models.Home.Home import Home
from multipledispatch import dispatch


class HomeController:

    def __init__(self, home: Home):
        self.home = home

    @dispatch(HomeRooms, DeviceType)
    def turn_on_device(self, room: HomeRooms, device_type: DeviceType):
        self.home[room].devices[device_type].turn_on()

    @dispatch(HomeRooms, DeviceType, str)
    def turn_on_device(self, room: HomeRooms, device_type: DeviceType, mode: str):
        pass

    def turn_off_device(self, room: HomeRooms, device_type: DeviceType):
        self.home[room].devices[device_type].turn_off()
