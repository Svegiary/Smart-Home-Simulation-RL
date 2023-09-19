from abc import ABC, abstractmethod


class Device(ABC):

    def __init__(self, name, controller, device_type):
        self.name = name
        self.controller = controller
        self.device_type = device_type

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def state(self):
        pass
