from abc import ABC, abstractmethod

from models.Devices.DeviceState import DeviceState


class ACState(DeviceState, ABC):
    def __init__(self, power_consumption):
        super.__init__(power_consumption)

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
        return super().power_consumption()


class HeatingState(ACState):
    def __init__(self, power_consumption):
        super().__init__(power_consumption)

    def turn_off(self):

        print("Turning AC off")

    def set_heating(self):
        print("AC in heating mode")

    def set_cooling(self):
        print("AC in cooling mode")


class CoolingState(ACState):
    def __init__(self, power_consumption):
        super().__init__(power_consumption)

    def turn_off(self):
        print("Turning off AC")

    def set_heating(self):
        print("AC in heating mode")

    def set_cooling(self):
        print("AC in Cooling mode")


class OffState(ACState):
    def __init__(self):
        super().__init__(0)

    def turn_off(self):
        print("The device is OFF")

    def set_heating(self):
        print("AC is heating mode")

    def set_cooling(self):
        print("AC in Cooling mode")
