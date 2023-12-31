"""
Represents a device
"""

from models.devices.device import Device
from collections import OrderedDict


class RepresentDevice:

    @staticmethod
    def print(device: Device) -> None:
        """
        Represent a device
        """
        ordered_attributes = OrderedDict()
        ordered_attributes["Name"] = device.name
        ordered_attributes["State"] = device.state
        ordered_attributes.update(vars(device.state))

        print("------------------------------")
        for attr_name, attr_value in ordered_attributes.items():
            print(f"{attr_name}: {attr_value}")

        print("------------------------------")
