"""
Concrete implementations of ac commands
"""
from models.command.device_command import DeviceCommand
from models.devices.ac.ac import AirConditioner


class ACSetCoolingCommand(DeviceCommand):
    def __init__(self, ac: AirConditioner) -> None:
        self.ac = ac

    def execute(self) -> None:
        self.ac.set_cooling()


class ACSetHeatingCommand(DeviceCommand):
    def __init__(self, ac: AirConditioner) -> None:
        self.ac = ac

    def execute(self) -> None:
        self.ac.set_heating()


class ACTurnOffCommand(DeviceCommand):
    def __init__(self, ac: AirConditioner) -> None:
        self.ac = ac

    def execute(self) -> None:
        self.ac.turn_off()
