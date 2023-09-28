"""
Class for creating devices. A simple if else factory, probably redundant when the logic 
is simple
"""

from models.devices.dehumidifier.dehumidifier import Dehumidifier
from models.devices.device import Device
from models.devices.light_bulb.light_bulb import LightBulb
from enums.DeviceType import DeviceType
from models.devices.ac.ac import AirConditioner


class DeviceFactory:

    @staticmethod
    def create_device(device_type: DeviceType, name: str, power_consumption: int) -> Device:
        if device_type == DeviceType.LIGHT:
            return LightBulb(name, power_consumption)
        elif device_type == DeviceType.AC:
            return AirConditioner(name, power_consumption)
        elif device_type == DeviceType.DEHUMIDIFIER:
            return Dehumidifier(name, power_consumption)
