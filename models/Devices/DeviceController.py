from abc import ABC, abstractmethod


class DeviceController(ABC):

    def __init__(self, state):
        self._state = state

    @abstractmethod
    def _setState(self, state):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def state(self):
        pass
