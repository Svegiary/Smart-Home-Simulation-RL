from typing import List

from representation.SensorRepresenation.RepresentSensor import RepresentSensor
from models.Sensors.Sensor import Sensor


class PrintSensors:

    @staticmethod
    def print(sensors: List[Sensor]):
        for sensor in sensors:
            RepresentSensor.print(sensor)
