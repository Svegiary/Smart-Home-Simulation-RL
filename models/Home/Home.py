import string
from typing import List, Dict

from enums.Rooms import HomeRooms

from models.Devices.Device import Device
from models.Home.Rooms.Rooms import Room


class Home:
    def __init__(self, rooms: Dict[HomeRooms, Room]):
        self.rooms: Dict[HomeRooms, Room] = {room.name: room for room in rooms}
        self.house_temp = 0
        self.house_light = 0
        self.house_humidity = 0
        # TODO: noise level

    def __getitem__(self, room):
        return self.rooms.get(room, None)

    # Setter for house_temp
    def set_house_temp(self, temp):
        self.house_temp = temp

    # Setter for house_light
    def set_house_light(self, light):
        self.house_light = light

    # Setter for house_humidity
    def set_house_humidity(self, humidity):
        self.house_humidity = humidity
