"""
Simple factory to create commands for the light bulb
"""

from models.command.light_bulb_commands import *
from models.devices.light_bulb.light_bulb import LightBulb


class LightBulbCommandFactory:

    @staticmethod
    def create_commands(light: LightBulb) -> list[DeviceCommand]:
        commands = []
        commands.append(TurnOnLight(light))
        commands.append(TurnOffLight(light))
        for step in range(10, 110, 10):
            commands.append(SetLightBrightness(light, step))
        return commands
