from typing import Dict, List

from models.Devices.StateRepresentation.StateRepresentation import RepresentState
from models.Devices.Device import Device
from enums.DeviceType import DeviceType


class PrintDevices:

    @staticmethod
    def print(devices: Dict[DeviceType, Device]):
        print(devices.items())
        for device_type, device in devices.items():
            print(device)
            RepresentState.print(device)
