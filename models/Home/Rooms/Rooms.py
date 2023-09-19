from abc import ABC, abstractmethod
from ast import List
from typing import Dict

from enums.Rooms import HomeRooms

from models.Devices.StateRepresentation.StateRepresentation import RepresentState

from models.Devices.Device import Device
from models.Sensors.Sensor import Sensor
from enums.DeviceType import DeviceType


class Room():

    def __init__(self, name: HomeRooms):
        self.name = name
        self.devices: Dict[DeviceType, Device] = {
        }
        self.sensors = []  # TODO: implement sensor abstract class
        self.is_human_inside = False

    def attach_device(self, device: Device):
        self.devices[device.device_type] = device

    def detach_device(self, device_type: DeviceType):
        if device_type in self.devices:
            del self.devices[device_type]

    def attach_sensor(self, sensor: Sensor):
        self.sensors.append(sensor)

    def detach_sensor(self, sensor: Sensor):
        return self.sensors.remove(sensor)

    def print_devices_and_state(self):
        for device in self.devices:
            RepresentState.print(device)

    def print_sensors(self):
        for sensor in self.sensors:
            print(sensor)
