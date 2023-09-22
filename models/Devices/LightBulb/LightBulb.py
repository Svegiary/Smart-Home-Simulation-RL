from enums.DeviceType import DeviceType
from models.Devices.Device import Device
from models.Devices.LightBulb.LightBulbState import *


class LightBulb(Device):
    def __init__(self, name, power_consumption):
        super().__init__(name, DeviceType.LIGHT, power_consumption, OffState())

    def turn_on(self):
        self.state.turn_on()
        self.state = OnState()
        return self.state

    def turn_off(self):
        self.state.turn_off()
        self.state = OffState()
        return self.state

    def set_brightness(self, brightness):
        self.state.set_brightness(brightness)
        return self.state
