from abc import ABC, abstractmethod


class DeviceState(ABC):

    def __init__(self, power_consumption):
        self._power_consumption = power_consumption

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    @property
    def power_consumption(self):
        pass
