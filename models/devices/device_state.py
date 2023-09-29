"""
-DeviceState.py
This file contains the abstract class for a Device state
All Devices must have a current_power (subject to change) attribute to 
save the current power consumption and a turn_off method to turn off the device
"""


from abc import ABC, abstractmethod


class DeviceState(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def power_consumption(self) -> int:
        pass
