"""
-LightBulbState.py
This file containts the concrete implementation of a LightBulbState class
and its discrete concrete statesS
Its' responsibilities:
1) Implement a common interface for all LightBulb States from the Device State class
2) Implement concrete states of the device and their methods
3) Calculate power consumption for each state. Here an OnState can
have different power consumption based on its brightness 
"""

from abc import ABC, abstractmethod
from models.devices.device_state import DeviceState


class LightBulbState(DeviceState, ABC):

    # Constructor for the abstract LightBulbState class
    def __init__(self, brightness: int):
        super().__init__()
        self._brightness = brightness

    # Abstract method to turn on the light bulb
    @abstractmethod
    def turn_on(self):
        pass

    # Abstract method to turn off the light bulb
    @abstractmethod
    def turn_off(self):
        pass

    # Abstract method to set the brightness of the light bulb

    @abstractmethod
    def set_brightness(brightness):
        pass

    # Abstract property to get the power consumption of the light bulb

    @property
    @abstractmethod
    def power_consumption(self):
        pass

# Define a concrete class OnState that inherits from LightBulbState


class OnState(LightBulbState):

    # Constructor for the OnState class
    def __init__(self):
        self._brightness = 100

        # Call the constructor of the parent class (LightBulbState) and initialize brightness and color_temp
        super().__init__(self._brightness)

    # Method to turn on the light bulb
    def turn_on(self) -> LightBulbState:
        print("The light bulb is on")

    # Method to turn off the light bulb
    def turn_off(self) -> LightBulbState:
        print("Turning off light bulb")

    # Method to set the brightness of the light bulb

    def set_brightness(self, brightness) -> LightBulbState:
        self._brightness = brightness

    def power_consumption(self, power) -> int:
        return power * (self._brightness / 100)


# Define a concrete class OffState that inherits from LightBulbState


class OffState(LightBulbState):

    # Constructor for the OffState class
    def __init__(self):
        brightness = 0

        # Call the constructor of the parent class (LightBulbState) and initialize brightness and color_temp
        super().__init__(brightness)

    # Method to turn on the light bulb
    def turn_on(self) -> None:
        print("Turning on light bulb")

    # Method to turn off the light bulb
    def turn_off(self) -> None:
        print("The Light Bulb is off")

    # Method to set the brightness of the light bulb

    def set_brightness(self, brightness) -> None:
        print("The Light Bulb is off")

    def power_consumption(self, power) -> int:
        return 0
