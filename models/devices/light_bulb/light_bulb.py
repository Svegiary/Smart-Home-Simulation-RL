"""
-LightBulb.py
This class implements the LightBulb Device
Its' responsibilities:
1) Set the state of the device to off, give it a name, add the device type and power consumption
2) Manage state transitions
3) Control the LightBulb
4) Get current power consumption based on the state of the device (to implement correctly)


"""


from enums.DeviceType import DeviceType
from models.devices.device import Device
from models.devices.light_bulb.light_bulb_state import *

# Define a class for a LightBulb that inherits from Device
# chat gpt comments


class LightBulb(Device):

    # Initialize the LightBulb object with a name and power consumption
    def __init__(self, name, power_consumption):
        # Call the constructor of the parent class (Device) using super()
        # Pass the name, device type (LIGHT), power consumption, and the initial state (OffState())
        super().__init__(name, DeviceType.LIGHT, power_consumption, OffState())

    # Method to turn on the LightBulb
    def turn_on(self) -> LightBulbState:
        # Call the turn_on method of the current state object
        self.state.turn_on()
        # Update the current state to OnState()
        self.state = OnState()
        # Return the new state
        return self.state

    # Method to turn off the LightBulb
    def turn_off(self) -> LightBulbState:
        # Call the turn_off method of the current state object
        self.state.turn_off()
        # Update the current state to OffState()
        self.state = OffState()
        # Return the new state
        return self.state

    # Method to set the brightness of the LightBulb
    def set_brightness(self, brightness: int) -> LightBulbState:
        # Call the set_brightness method of the current state object
        self.state.set_brightness(brightness)
        # Return the new state
        return self.state

    def current_power(self) -> int:
        return super().power_consumption(self.power_consumption)
