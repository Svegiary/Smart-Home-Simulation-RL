from enums.DeviceType import DeviceType
from models.Devices.Dehumidifier.DehumidifierSate import OffState, OnState
from models.Devices.Device import Device


class Dehumidifier(Device):

    def __init__(self, name, power_consumption):
        super().__init__(name, DeviceType.DEHUMIDIFIER, power_consumption, OffState())

    def turn_off(self):
        self.state.turn_off()
        self.state = OffState()
        return self.state

    def turn_on(self):
        self.state.turn_on()
        self.state = OnState()
        return self.state

    @property
    def current_power(self):
        return self.state.power_consumption
