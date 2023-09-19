from models.Devices.StateRepresentation.StateRepresentation import RepresentState
from models.Home.Home import Home
from models.Home.HomeRepresentation.PrintDevices import PrintDevices
from models.Home.HomeRepresentation.PrintSensors import PrintSensors
from models.Sensors.RepresentSensor import RepresentSensor


class PrintHome:
    @staticmethod
    def print(home: Home):
        print("###############################################################")

        for room_name, room_instance in home.rooms.items():
            print(room_name, " : ")
            PrintDevices.print(room_instance.devices)
            PrintSensors.print(room_instance.sensors)
        print("###############################################################")
