"""
-invoker.py
For controlling the devices I am using the command pattern
This file is responsible for the mechanism that the commands will be executed
and it keeps a history of all the commands 
"""

from models.command.device_command import DeviceCommand


class Invoker:
    """
    For controlling the devices I am using the command pattern
    This file is responsible for the mechanism that the commands will be executed
    and it keeps a history of all the commands 
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Invoker, cls).__new__(cls)
            cls._instance.command_history = []
        return cls._instance

    def execute(self, command: DeviceCommand) -> None:
        command.execute()
        self.command_history.append(command)
