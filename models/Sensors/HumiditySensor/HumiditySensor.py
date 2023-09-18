from main import Sensor


class HumiditySensor(Sensor):
    def __init__(self, temp_limit, name) -> None:
        self.temp_limit = temp_limit
        super().__init__(name)

    def trigger(self):
        self.triggered = not self.triggered
