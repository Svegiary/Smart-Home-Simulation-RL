from models.Device import Device
from collections import OrderedDict


class RepresentState:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RepresentState, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def print(device: Device):
        ordered_attributes = OrderedDict()
        ordered_attributes["Name"] = device.name
        ordered_attributes["State"] = device.state
        ordered_attributes.update(vars(device.state))

        print("------------------------------")
        for attr_name, attr_value in ordered_attributes.items():
            print(f"{attr_name}: {attr_value}")

        print("------------------------------")
