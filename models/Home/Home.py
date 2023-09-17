import string

from models.Devices.Device import Device


class Home:
    def __init__(self):
        self.room_devices = {}

    def addDevice(self, room: string, device: Device):
        self.room_devices[room] = device
