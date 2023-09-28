"""
-ACState.py
This file containts the concrete implementation of an ACState class
and its discrete concrete statesS
Its' responsibilities:
1) Implement a common interface for all AC States from the Device State class
2) Implement concrete states of the device and their methods
3) Calculate power consumption for each state
"""
from abc import ABC, abstractmethod

# Import the base class DeviceState from another module
from models.devices.device_state import DeviceState

# Define an abstract base class ACState that inherits from DeviceState and ABC (Abstract Base Class)
# Chat gpt generated comments bellow sorry


class ACState(DeviceState, ABC):

    # Constructor for the abstract ACState class
    def __init__(self):
        super().__init__()

    # Abstract method to turn off the AC device
    @abstractmethod
    def turn_off(self):
        pass

    # Abstract method to set the AC device to heating mode
    @abstractmethod
    def set_heating(self):
        pass

    # Abstract method to set the AC device to cooling mode
    @abstractmethod
    def set_cooling(self):
        pass

    # Abstract property to get the power consumption of the AC device
    @property
    @abstractmethod
    def power_consumption(self):
        pass

# Define a concrete class HeatingState that inherits from ACState


class HeatingState(ACState):

    # Constructor for the HeatingState class
    def __init__(self):
        super().__init__()

    # Method to turn off the AC device
    def turn_off(self):
        print("Turning AC off")

    # Method to set the AC device to heating mode
    def set_heating(self):
        print("AC in heating mode")

    # Method to set the AC device to cooling mode
    def set_cooling(self):
        print("AC in cooling mode")

    # Property to get the power consumption of the AC device when in this state
    @property
    def power_consumption(self):
        self.current_power = 2000  # Assuming a power consumption of 2000 watts
        return 2000

# Define a concrete class CoolingState that inherits from ACState


class CoolingState(ACState):

    # Constructor for the CoolingState class
    def __init__(self):
        super().__init__()

    # Method to turn off the AC device
    def turn_off(self):
        print("Turning off AC")

    # Method to set the AC device to heating mode
    def set_heating(self):
        print("AC in heating mode")

    # Method to set the AC device to cooling mode
    def set_cooling(self):
        print("AC in Cooling mode")

    # Property to get the power consumption of the AC device when in this state
    @property
    def power_consumption(self):
        self.current_power = 2000  # Assuming a power consumption of 2000 watts
        return 2000

# Define a concrete class OffState that inherits from ACState


class OffState(ACState):

    # Constructor for the OffState class
    def __init__(self):
        super().__init__()

    # Method to turn off the AC device
    def turn_off(self):
        print("The device is OFF")

    # Method to set the AC device to heating mode
    def set_heating(self):
        print("AC is heating mode")

    # Method to set the AC device to cooling mode
    def set_cooling(self):
        print("AC in Cooling mode")

    # Method to get the power consumption of the AC device when in this state
    def power_consumption(self):
        self.current_power = 0  # Assuming zero power consumption when off
        return 0
