from enums.DeviceType import DeviceType
from models.Devices.Device import Device
from models.Devices.LightBulb.LightBulbController import LightBulbController


class LightBulb(Device):
    def __init__(self, name, cont, power_consumption):

        super().__init__(name, cont, DeviceType.LIGHT, power_consumption)

    @property
    def state(self):
        return self.controller.state
