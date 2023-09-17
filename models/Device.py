from abc import ABC, abstractmethod


class Device(ABC):

    def __init__(self, name, controller):
        self.name = name
        self.controller = controller

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def state(self):
        pass
