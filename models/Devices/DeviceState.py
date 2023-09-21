from abc import ABC, abstractmethod


class DeviceState(ABC):

    def __init__(self, power_consumption):
        self.current_power = power_consumption

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def power_consumption(self):
        pass
