from models.Command.DehumidifierCommands import TurnOffDehumidifier, TurnOnDehumidifier
from models.Devices.Dehumidifier.Dehumidifier import Dehumidifier


class DehumidifierCommandFactory:
    def __init__(self, dehumidifier: Dehumidifier):
        self.dehumidifier = dehumidifier
        self.commands = []

    def create_commands(self):
        self.commands.append(TurnOnDehumidifier(self.dehumidifier))
        self.commands.append(TurnOffDehumidifier(self.dehumidifier))
