"""
Simple class for representing the house. Possible 
extension to a gui
"""

from models.home.home import Home
from representation.home_representation.print_devices import PrintDevices
from representation.home_representation.print_sensors import PrintSensors


class PrintHome:
    @staticmethod
    def print(home: Home) -> None:
        print("###############################################################")

        for room_name, room_instance in home.rooms.items():
            print(room_name, " : ")
            PrintDevices.print(room_instance.devices)
            PrintSensors.print(room_instance.sensors)
        print("###############################################################")
