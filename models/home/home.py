"""
-home.py
This is the class that represents the home structure
Each home has rooms , the internal data and a human that 
can be placed in rooms
"""


from typing import Dict

from enums.Rooms import HomeRooms

from models.home.rooms.rooms import Room
from simulation.human.human import Human


class Home:
    def __init__(self, rooms: list[Room]):
        self.rooms: Dict[HomeRooms, Room] = {room.name: room for room in rooms}
        self.house_temp: float = 0.0
        self.house_light: float = 0.0
        self.house_humidity: float = 0.0
        self.human: Human = Human()
        # TODO: noise level

    def __getitem__(self, room: HomeRooms) -> Room:
        return self.rooms.get(room, None)

    # Setter for house_temp
    def set_house_temp(self, temp: float) -> None:
        self.house_temp = temp

    # Setter for house_light
    def set_house_light(self, light: float) -> None:
        self.house_light = light

    # Setter for house_humidity
    def set_house_humidity(self, humidity: float) -> None:
        self.house_humidity = humidity

    # Place a human in a room
    def place_human(self, room: HomeRooms) -> None:

        self.human.place_human(self.rooms[room])
