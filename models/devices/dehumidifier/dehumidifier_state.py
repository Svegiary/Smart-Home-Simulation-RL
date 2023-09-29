
"""
-Dehumidiertate.py
This file containts the concrete implementation of an DehumidifierState class
and its discrete concrete statesS
Its' responsibilities:
1) Implement a common interface for all Dehumidier States from the Device State class
2) Implement concrete states of the device and their methods
3) Calculate power consumption for each state
"""


from abc import ABC, abstractmethod
from models.devices.device_state import DeviceState


class DehumidifierState(DeviceState, ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def turn_off(self) -> None:
        pass

    @abstractmethod
    def turn_on(self) -> None:
        pass

    def power_consumption(self):
        pass


class OffState(DehumidifierState):
    def __init__(self):
        super().__init__()

    def turn_off(self) -> None:
        print("Dehumidifier is off")

    def turn_on(self) -> None:
        print("Turing on Dehumidier")

    def power_consumption(self, power) -> int:
        return 0


class OnState(DehumidifierState):
    def __init__(self):
        super().__init__()

    def turn_off(self) -> None:
        print("Turing off Dehumidier")

    def turn_on(self) -> None:
        print("Dehumidifier is on")

    def power_consumption(self, power) -> int:
        return power
