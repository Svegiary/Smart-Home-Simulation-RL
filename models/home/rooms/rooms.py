"""
-rooms.py
"""


from typing import Dict

from enums.Rooms import HomeRooms


from models.devices.device import Device
from models.Sensors.Sensor import Sensor
from enums.DeviceType import DeviceType


class Room:
    """
    This file contains the representation of a room,
    A room has devices , sensors , a name from the HomeRooms enum and 
    a boolean wether a human is inside the room (mainly for debugging / easy visualisation)

    It also allows for attaching and detaching devices and sensors to the room 
    and also placing the human inside (changing the boolean to true)
    """

    def __init__(self, name: HomeRooms):
        self.name: HomeRooms = name
        self.devices: Dict[DeviceType, Device] = {
        }

        self.sensors: list[Sensor] = []
        self.is_human_inside: bool = False
        self.luminance: float = 0.0

    def attach_device(self, device: Device) -> None:
        """Attach a device to the room"""
        self.devices[device.device_type] = device

    def detach_device(self, device_type: DeviceType) -> None:
        """Detach a device from the room"""
        if device_type in self.devices:
            del self.devices[device_type]

    def attach_sensor(self, sensor: Sensor) -> None:
        """Attach a sensor to the room"""
        self.sensors.append(sensor)

    def detach_sensor(self, sensor: Sensor) -> None:
        """Attach a sensor to the room"""
        return self.sensors.remove(sensor)

    def place_human(self) -> None:
        """Place a human to this room"""
        self.is_human_inside = True
