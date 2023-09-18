from typing import List

from models.Devices.StateRepresentation.StateRepresentation import RepresentState
from models.Sensors.PrintSensors import RepresentSensor
from models.Sensors.Sensor import Sensor


class PrintSensors:

    @staticmethod
    def print(sensors: List[Sensor]):
        for sensor in sensors:
            RepresentSensor.print(sensor)
