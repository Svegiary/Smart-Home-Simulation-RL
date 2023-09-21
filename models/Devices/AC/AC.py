from enums.DeviceType import DeviceType
from models.Devices.Device import Device


class AirConditioner(Device):

    def __init__(self, name, controller, power_consumption):
        super().__init__(name, controller,  DeviceType.AC, power_consumption)

    @property
    def state(self):
        return self.controller.state
