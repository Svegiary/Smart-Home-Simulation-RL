"""
Concrete implementations of light bulb commands
"""
from models.command.device_command import DeviceCommand
from models.devices.light_bulb.light_bulb import LightBulb


class TurnOnLight(DeviceCommand):
    def __init__(self, light_bulb: LightBulb) -> None:
        self.light_bulb = light_bulb

    def execute(self) -> None:
        self.light_bulb.turn_on()


class TurnOffLight:
    def __init__(self, light_bulb: LightBulb) -> None:
        self.light_bulb = light_bulb

    def execute(self):
        self.light_bulb.turn_off()


class SetLightBrightness:
    def __init__(self, light_bulb: LightBulb, brightness: int) -> None:
        self.light_bulb = light_bulb
        self.brightness = brightness

    def execute(self):
        self.light_bulb.set_brightness(self.brightness)
