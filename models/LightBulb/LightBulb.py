from models.Device import Device
from models.LightBulb.LightBulbController import LightBulbController


class LightBulb(Device):
    def __init__(self, name):
        super().__init__(name, LightBulbController())

    def turn_on(self):
        self.controller.turn_on()

    def turn_off(self):
        self.controller.turn_off()

    def set_color_temp(self, color_temp):
        self.controller.set_color_temp(color_temp)

    def set_brightness(self, brightness):
        self.controller.set_brightness(brightness)

    @property
    def state(self):
        return self.controller.state

    @property
    def power_consumption(self):
        return self._state.power_consumption
