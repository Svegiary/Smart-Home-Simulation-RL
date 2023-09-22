from models.Devices.Command.DeviceCommand import DeviceCommand
from models.Devices.LightBulb.LightBulb import LightBulb


class TurnOnLight(DeviceCommand):
    def __init__(self, light_bulb: LightBulb):
        self.light_bulb = light_bulb

    def execute(self):
        self.light_bulb.turn_on()


class TurnOffLight:
    def __init__(self, light_bulb: LightBulb):
        self.light_bulb = light_bulb

    def execute(self):
        self.light_bulb.turn_off()


class SetLightBrightness:
    def __init__(self, light_bulb: LightBulb, brightness: int):
        self.light_bulb = light_bulb
        self.brightness = brightness

    def execute(self):
        self.light_bulb.set_brightness(self.brightness)
