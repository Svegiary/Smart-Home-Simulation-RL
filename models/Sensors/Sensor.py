from abc import ABC, abstractmethod


class Sensor(ABC):

    def __init__(self, name):
        self.name = name
        self.triggered = False

    @abstractmethod
    def trigger(self):
        pass
