from abc import ABC, abstractmethod


class DeviceCommand(ABC):

    @abstractmethod
    def execute(self):
        pass
