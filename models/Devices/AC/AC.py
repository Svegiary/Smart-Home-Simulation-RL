from enums.DeviceType import DeviceType
from models.Devices.AC.ACState import *
from models.Devices.Device import Device


class AirConditioner(Device):

    def __init__(self, name,  power_consumption):
        super().__init__(name, DeviceType.AC, power_consumption, OffState())

    def set_heating(self):
        self.state.set_heating()
        self.state = HeatingState()
        return self.state

    def set_cooling(self):
        self.state.set_cooling()
        self.state = CoolingState()
        return self.state

    def turn_off(self):
        self.state.turn_off()
        self.state = OffState()
        return self.state

    @property
    def current_power(self):
        return self.state.power_consumption()
