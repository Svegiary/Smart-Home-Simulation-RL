from abc import ABC, abstractmethod

from models.Devices.DeviceState import DeviceState


class ACState(DeviceState, ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def set_heating(self):
        pass

    @abstractmethod
    def set_cooling(self):
        pass

    @property
    def power_consumption(self):
        pass


class HeatingState(ACState):

    def __init__(self):
        super().__init__()

    def turn_off(self):

        print("Turning AC off")

    def set_heating(self):
        print("AC in heating mode")

    def set_cooling(self):
        print("AC in cooling mode")

    @property
    def power_consumption(self):
        self.current_power = 2000
        return 2000


class CoolingState(ACState):

    def __init__(self):
        super().__init__()

    def turn_off(self):
        print("Turning off AC")

    def set_heating(self):
        print("AC in heating mode")

    def set_cooling(self):
        print("AC in Cooling mode")

    @property
    def power_consumption(self):
        self.current_power = 2000
        return 2000


class OffState(ACState):

    def __init__(self):
        super().__init__()

    def turn_off(self):
        print("The device is OFF")

    def set_heating(self):
        print("AC is heating mode")

    def set_cooling(self):
        print("AC in Cooling mode")

    def power_consumption(self):
        self.current_power = 0
        return 0
