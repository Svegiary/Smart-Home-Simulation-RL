"""
-invoker.py
For controlling the devices I am using the command pattern
This file is responsible for the mechanism that the commands will be executed
and it keeps a history of all the commands 
"""

from models.command.device_command import DeviceCommand


class Invoker:
    def __init__(self) -> None:
        self.command_history = []

    def execute(self, command: DeviceCommand) -> None:
        command.execute()
        self.command_history.append(command)
