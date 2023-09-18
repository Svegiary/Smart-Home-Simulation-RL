from models.Devices.StateRepresentation.StateRepresentation import RepresentState
from models.Home.Home import Home
from models.Home.HomeRepresentation.PrintDevices import PrintDevices
from models.Home.HomeRepresentation.PrintSensors import PrintSensors
from models.Sensors.PrintSensors import RepresentSensor


class PrintHome:
    @staticmethod
    def print(home: Home):
        print("###############################################################")

        for room in home.rooms:
            print(room.name, " : ")
            PrintDevices.print(room.devices)
            PrintSensors.print(room.sensors)
        print("###############################################################")
