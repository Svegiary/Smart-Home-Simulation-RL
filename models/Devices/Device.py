from abc import ABC, abstractmethod
from enums.DeviceType import DeviceType

from models.Devices.DeviceState import DeviceState


class Device(ABC):

    def __init__(self, name, device_type: DeviceType, power_consumption, state: DeviceState):
        self.name = name
        self.device_type: DeviceType = device_type
        self.power_consumption = power_consumption
        self.state = state
