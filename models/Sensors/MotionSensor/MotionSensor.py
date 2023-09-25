from enums.MotionSensorEvents import MotionSensorEvent
from models.Sensors.Sensor import Sensor


class MotionSensor(Sensor):
    def __init__(self, name):
        super().__init__(name)

    def trigger(self):
        pass
