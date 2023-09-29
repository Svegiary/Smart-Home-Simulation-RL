"""
Searches for device states that might change the simulation state
"""

from models.devices.ac.ac import AirConditioner
from models.devices.ac.ac_state import OffState
from models.devices.dehumidifier.dehumidifier import Dehumidifier
from models.devices.device import Device
from models.devices.light_bulb.light_bulb import LightBulb
from models.home.home import Home
from enums.DeviceType import DeviceType


class HomeDeviceSnapshot:
    _instance = None

    def __new__(cls, home: Home):
        if cls._instance is None:
            cls._instance = super(HomeDeviceSnapshot, cls).__new__(cls)
            cls._instance.initialize(home)
        return cls._instance

    def initialize(self, home: Home):
        self.home = home
        self.active_acs: list[AirConditioner] = []
        self.active_lights: list[LightBulb] = []
        self.active_dehumidifers: list[Dehumidifier] = []
        self.active_devices: list[Device] = []

    def count_ac(self):
        active_ac = []
        for room in self.home.rooms.values():
            for key, device in room.devices.items():
                if device.device_type == DeviceType.AC and not isinstance(device.state, OffState):
                    active_ac.append(device)
        self.active_acs = active_ac

    def count_lights(self):
        active_lights = []
        for key, value in self.home.rooms.items():
            for key, device in value.devices.items():
                if device.device_type == DeviceType.LIGHT:
                    active_lights.append(device)
        self.active_lights = active_lights

    def count_dehumidifers(self):
        active_dehumidiers = []
        for room in self.home.rooms.values():
            for key, device in room.devices.items():
                if device.device_type == DeviceType.DEHUMIDIFIER:
                    active_dehumidiers.append(device)
        self.active_dehumidifers = active_dehumidiers

    def count_all(self) -> None:
        self.count_ac()
        self.count_lights()
        self.count_dehumidifers()
        self.active_devices = self.active_acs + \
            self.active_lights + self.active_dehumidifers
