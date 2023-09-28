"""
device_command.py
This file contains the abstract base class for all device commands.
"""

from abc import ABC, abstractmethod


class DeviceCommand(ABC):

    @abstractmethod
    def execute(self):
        pass
