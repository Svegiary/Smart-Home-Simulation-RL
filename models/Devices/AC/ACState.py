from abc import ABC, abstractmethod

from models.Devices.DeviceState import DeviceState


class ACState(DeviceState, ABC):
    def __init__(self, power_consumption):
        super.__init__(power_consumption)

    @abstractmethod
    def turn_on(self):
        pass
