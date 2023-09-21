from abc import ABC, abstractmethod

from models.Devices.Actions.Action import Action
from models.Devices.DeviceState import DeviceState


class DeviceController(ABC):

    def __init__(self, state):
        self._state = state

        self.actions: list[Action] = []

    @abstractmethod
    def initialize_controller(self, actions):
        pass

    @abstractmethod
    def _setState(self, state):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def state(self) -> DeviceState:
        pass
