"""
Concrete implementations of dehumidifier commands
"""

from models.command.device_command import DeviceCommand
from models.devices.dehumidifier.dehumidifier import Dehumidifier


class TurnOnDehumidifier(DeviceCommand):
    def __init__(self, dehumidifier: Dehumidifier) -> None:
        self.dehumidifier = dehumidifier

    def execute(self) -> None:
        self.dehumidifier.turn_on()


class TurnOffDehumidifier(DeviceCommand):
    def __init__(self, dehumidifier: Dehumidifier) -> None:
        self.dehumidifier = dehumidifier

    def execute(self) -> None:
        self.dehumidifier.turn_off()
