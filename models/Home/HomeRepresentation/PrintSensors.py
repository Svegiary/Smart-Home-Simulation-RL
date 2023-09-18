from collections import OrderedDict
from models.Sensors.Sensor import Sensor


class RepresentSensor:

    @staticmethod
    def print(sensor: Sensor):
        ordered_attributes = OrderedDict()
        ordered_attributes["Name"] = sensor.name
        ordered_attributes.update(vars(sensor))

        print("------------------------------")
        for attr_name, attr_value in ordered_attributes.items():
            print(f"{attr_name}: {attr_value}")

        print("------------------------------")
