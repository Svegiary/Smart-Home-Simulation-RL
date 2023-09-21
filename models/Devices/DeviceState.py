from abc import ABC, abstractmethod


class DeviceState(ABC):

    def __init__(self):
        self.current_power = 0

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def power_consumption(self):
        pass
