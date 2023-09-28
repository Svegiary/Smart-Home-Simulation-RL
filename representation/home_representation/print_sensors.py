"""
Simple class for representing the sensors 
"""
from typing import List

from representation.sensor_represenation.represent_sensor import RepresentSensor
from models.Sensors.Sensor import Sensor


class PrintSensors:

    @staticmethod
    def print(sensors: List[Sensor]) -> None:
        for sensor in sensors:
            RepresentSensor.print(sensor)
