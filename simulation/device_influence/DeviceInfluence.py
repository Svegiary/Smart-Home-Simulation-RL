from models.Home.Home import Home
from enums.Rooms import HomeRooms
from enums.DeviceType import DeviceType


class DeviceInfluence:

    def __init__(self, home: Home):
        self.home = home

    def ac_is_on(self):
        if self.home.rooms[HomeRooms.LIVING_ROOM].devices[DeviceType.AC]:  # TODO: cont
            pass
