from models.Home.Home import Home
from representation.HomeRepresentation.PrintDevices import PrintDevices
from representation.HomeRepresentation.PrintSensors import PrintSensors

from representation.SensorRepresenation.RepresentSensor import RepresentSensor


class PrintHome:
    @staticmethod
    def print(home: Home):
        print("###############################################################")

        for room_name, room_instance in home.rooms.items():
            print(room_name, " : ")
            PrintDevices.print(room_instance.devices)
            PrintSensors.print(room_instance.sensors)
        print("###############################################################")
