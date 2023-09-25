from models.Command.LightBulbCommands import *
from models.Devices.LightBulb.LightBulb import LightBulb


class LightBulbCommandFactory:

    def __init__(self, light: LightBulb) -> None:
        self.light = light
        self.commands = []

    def create_commands(self):
        self.commands.append(TurnOnLight(self.light))
        self.commands.append(TurnOffLight(self.light))
        for step in range(10, 110, 10):
            self.commands.append(SetLightBrightness(self.light, step))
