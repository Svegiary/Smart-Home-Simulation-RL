from models.Command.DeviceCommand import DeviceCommand
from models.Devices.Dehumidifier.Dehumidifier import Dehumidifier


class TurnOnDehumidifier(DeviceCommand):
    def __init__(self, dehumidifier: Dehumidifier):
        self.dehumidifier = dehumidifier

    def execute(self):
        self.dehumidifier.turn_on()


class TurnOffDehumidifier(DeviceCommand):
    def __init__(self, dehumidifier: Dehumidifier):
        self.dehumidifier = dehumidifier

    def execute(self):
        self.dehumidifier.turn_off()
