"""
-Dehumidifier.py
This class implements the Dehumidifier Device
Its' responsibilities:
1) Set the state of the device to off, give it a name, add the device type and power consumption
2) Manage state transitions
3) Control the Dehumidier
4) Get current power consumption based on the state of the device (to implement correctly)


"""


from models.devices.dehumidifier.dehumidifier_state import OffState, OnState
from enums.DeviceType import DeviceType
from models.devices.device import Device

# chat gpt comments


class Dehumidifier(Device):

    # Initialize the Dehumidifier object with a name and power consumption
    def __init__(self, name, power_consumption):
        # Call the constructor of the parent class (Device) using super()
        # Pass the name, device type (DEHUMIDIFIER), power consumption, and the initial state (OffState())
        super().__init__(name, DeviceType.DEHUMIDIFIER, power_consumption, OffState())

    # Method to turn off the Dehumidifier
    def turn_off(self):
        # Call the turn_off method of the current state object
        self.state.turn_off()
        # Update the current state to OffState()
        self.state = OffState()
        # Return the new state
        return self.state

    # Method to turn on the Dehumidifier
    def turn_on(self):
        # Call the turn_on method of the current state object
        self.state.turn_on()
        # Update the current state to OnState()
        self.state = OnState()
        # Return the new state
        return self.state

    # Property to get the current power consumption of the Dehumidifier
    @property
    def current_power(self):
        # Return the power consumption of the current state
        return self.state.power_consumption
