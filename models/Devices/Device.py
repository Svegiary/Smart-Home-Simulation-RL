from abc import ABC, abstractmethod


class Device(ABC):

    def __init__(self, name, controller):
        self.name = name
        self.controller = controller
        self.device_type = 0

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def state(self):
        pass
