"""
Simple factory to create commands for the dehumidifier.
"""

from models.command.dehumidifier_commands import TurnOffDehumidifier, TurnOnDehumidifier
from models.devices.dehumidifier.dehumidifier import Dehumidifier


class DehumidifierCommandFactory:
    def __init__(self, dehumidifier: Dehumidifier):
        self.dehumidifier = dehumidifier
        self.commands = []

    def create_commands(self):
        self.commands.append(TurnOnDehumidifier(self.dehumidifier))
        self.commands.append(TurnOffDehumidifier(self.dehumidifier))
