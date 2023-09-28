from typing import Dict, List

from models.devices.device import Device
from enums.DeviceType import DeviceType
from representation.StateRepresentation.StateRepresentation import RepresentState


class PrintDevices:

    @staticmethod
    def print(devices: Dict[DeviceType, Device]):
        print(devices.items())
        for device_type, device in devices.items():
            RepresentState.print(device)
