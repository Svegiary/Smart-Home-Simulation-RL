from main import Sensor


class TemperatureSensor(Sensor):
    def __init__(self, current_temp, name) -> None:
        self.current_temp = current_temp
        super().__init__(name)

    def set_current_temp(self, current_temp):
        self.current_temp = current_temp

    def trigger(self):
        self.triggered = not self.triggered
