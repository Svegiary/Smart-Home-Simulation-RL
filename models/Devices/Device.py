from abc import ABC, abstractmethod


class Device(ABC):

    def __init__(self, name, controller, device_type, power_consumption):
        self.name = name
        self.controller = controller
        self.device_type = device_type
        self.power_consumption = power_consumption

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def state(self):
        pass
