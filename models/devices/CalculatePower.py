from abc import ABC, abstractmethod
from models.Devices.Device import Device


class Power(ABC):
    def __init__(self):
        pass

    def calculate(device: Device):
        return device.state.power_consumption()
