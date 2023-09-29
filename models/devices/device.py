"""
-Device.py
This file contains the interface for the devices
Because devices differ a lot based on their functions
but not based on their attributes (name , state , etc) 
this file only provides an interface for those and the common to all devices
turn_off command
It's responsibilities:
1) Provide a common interface for the devices' constructors and the turn_off command

PS. The devices in this project have straight forward state transitions so these can be handled 
by the device itself without adding complexity.
However if the transitions were more complex , a device controller class would be beneficial
adhearing to solid principles and making the code more maintainable
"""

from abc import ABC, abstractmethod
from enums.DeviceType import DeviceType
from models.devices.device_state import DeviceState

# Define an abstract base class Device that inherits from ABC (Abstract Base Class)
# chat gpt


class Device(ABC):

    # Constructor for the Device class
    def __init__(self, name: str, device_type: DeviceType, power_consumption: int, state: DeviceState) -> None:
        # Initialize instance variables
        self.name = name
        self.device_type: DeviceType = device_type
        self.power_consumption = power_consumption
        self.state = state

    @abstractmethod
    def turn_off(self) -> DeviceState:
        pass

    def current_power(self) -> int:
        return self.state.power_consumption(self.power_consumption)
