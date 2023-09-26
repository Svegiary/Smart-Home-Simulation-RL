
from abc import ABC, abstractmethod
from models.Devices.DeviceState import DeviceState


class DehumidifierState(DeviceState, ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def turn_on(self):
        pass

    @property
    def power_consumption(self):
        pass


class OffState(DehumidifierState):
    def __init__(self):
        super().__init__()

    def turn_off(self):
        print("Dehumidifier is off")

    def turn_on(self):
        print("Turing on Dehumidier")

    @property
    def power_consumption(self):
        self.current_power = 0
        return 0


class OnState(DehumidifierState):
    def __init__(self):
        super().__init__()

    def turn_off(self):
        print("Turing off Dehumidier")

    def turn_on(self):
        print("Dehumidifier is on")

    @property
    def power_consumption(self):
        self.current_power = 100
        return 100
