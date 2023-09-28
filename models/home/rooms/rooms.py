"""
-rooms.py
This file contains the representation of a room,
A room has devices , sensors , a name from the HomeRooms enum and 
a boolean wether a human is inside the room (mainly for debugging / easy visualisation)

It also allows for attaching and detaching devices and sensors to the room 
and also placing the human inside (changing the boolean to true)

"""


from typing import Dict

from enums.Rooms import HomeRooms


from models.devices.device import Device
from models.Sensors.Sensor import Sensor
from enums.DeviceType import DeviceType


class Room:

    def __init__(self, name: HomeRooms):
        self.name: HomeRooms = name
        self.devices: Dict[DeviceType, Device] = {
        }

        # TODO: implement sensor abstract class
        self.sensors: list[Sensor] = []
        self.is_human_inside: bool = False

    def attach_device(self, device: Device) -> None:
        self.devices[device.device_type] = device

    def detach_device(self, device_type: DeviceType) -> None:
        if device_type in self.devices:
            del self.devices[device_type]

    def attach_sensor(self, sensor: Sensor) -> None:
        self.sensors.append(sensor)

    def detach_sensor(self, sensor: Sensor) -> None:
        return self.sensors.remove(sensor)

    def place_human(self) -> None:
        self.is_human_inside = True
