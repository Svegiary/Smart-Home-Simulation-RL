from typing import Dict, List
import string

from enums.Rooms import HomeRooms

from models.Devices.Device import Device
from models.Home.Rooms.Rooms import Room


class Home:
    def __init__(self, rooms: List[Room]):
        self.rooms: Dict[HomeRooms, Room] = {room.name: room for room in rooms}

    def __getitem__(self, room):
        return self.rooms.get(room, None)
