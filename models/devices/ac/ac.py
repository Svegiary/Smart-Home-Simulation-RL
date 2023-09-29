"""
-AC.py
This class implements the AirConditioner Device
Its' responsibilities:
1) Set the state of the device to off, give it a name, add the device type and power consumption
2) Manage state transitions
3) Control the AC
4) Get current power consumption based on the state of the device (to implement correctly)


"""


from enums.DeviceType import DeviceType
from models.devices.ac.ac_state import *
from models.devices.device import Device


class AirConditioner(Device):

    def __init__(self, name, power_consumption):

        super().__init__(name, DeviceType.AC, power_consumption, OffState())

    def set_heating(self) -> ACState:
        """
        Call the corresponding function of the state
        and change the state of the device

        """
        self.state.set_heating()
        self.state = HeatingState()
        return self.state

    def set_cooling(self) -> ACState:
        self.state.set_cooling()
        self.state = CoolingState()
        return self.state

    def turn_off(self) -> ACState:
        self.state.turn_off()
        self.state = OffState()
        return self.state

    def current_power(self) -> int:  # TODO: implement correctly
        return self.state.power_consumption(self.power_consumption)
