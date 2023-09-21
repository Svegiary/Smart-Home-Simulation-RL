from enums.DeviceType import DeviceType
from models.Devices.Device import Device


class AirConditioner(Device):

    def __init__(self, name, controller, power_consumption):
        super().__init__(name, controller,  DeviceType.AC, power_consumption)

    def turn_on(self):
        self.controller.turn_on()

    def turn_off(self):
        self.controller.turn_off()

    def set_heating(self):
        self.controller.set_heating()

    def set_cooling(self):
        self.controller.set_cooling()

    @property
    def state(self):
        return self.controller.state

    @property
    def power_consumption(self):
        return self.controller.state
