from models.Command.DeviceCommand import DeviceCommand


class Invoker:
    def __init__(self) -> None:
        self.command_history = []

    def execute(self, command: DeviceCommand):
        command.execute()
        self.command_history.append(command)
