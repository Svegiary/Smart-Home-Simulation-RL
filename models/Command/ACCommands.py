from models.Devices.AC.AC import AirConditioner
from models.Command.DeviceCommand import DeviceCommand
from models.Devices.Device import Device


class ACSetCoolingCommand(DeviceCommand):
    def __init__(self, ac: AirConditioner):
        self.ac = ac

    def execute(self):
        self.ac.set_cooling()


class ACSetHeatingCommand(DeviceCommand):
    def __init__(self, ac: AirConditioner):
        self.ac = ac

    def execute(self):
        self.ac.set_heating()


class ACTurnOffCommand(DeviceCommand):
    def __init__(self, ac: AirConditioner):
        self.ac = ac

    def execute(self):
        self.ac.turn_off()
