from typing import List
import string

from models.Devices.Device import Device
from models.Home.Rooms.Rooms import Room


class Home:
    def __init__(self, rooms):
        self.rooms: List[Room] = rooms
