from abc import ABC, abstractmethod
from enums.DeviceType import DeviceType

from models.Devices.DeviceController import DeviceController
from models.Devices.DeviceState import DeviceState


class Device(ABC):

    def __init__(self, name, controller: DeviceController, device_type: DeviceType, power_consumption):
        self.name = name
        self.controller: DeviceController = controller
        self.device_type: DeviceType = device_type
        self.power_consumption = power_consumption

    @abstractmethod
    def state(self) -> DeviceState:
        pass
