from abc import ABC, abstractmethod


class DeviceController(ABC):

    def __init__(self, state):
        self._state = state

    @abstractmethod
    def _setState(self, state):
        pass

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    @property
    def state(self):
        pass
