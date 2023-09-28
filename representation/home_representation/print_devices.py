"""
Simple print method for all devices

"""

from typing import Dict, List

from models.devices.device import Device
from enums.DeviceType import DeviceType
from representation.device_representation.device_representation import RepresentDevice


class PrintDevices:

    @staticmethod
    def print(devices: Dict[DeviceType, Device]) -> None:
        print(devices.items())
        for device_type, device in devices.items():
            RepresentDevice.print(device)
