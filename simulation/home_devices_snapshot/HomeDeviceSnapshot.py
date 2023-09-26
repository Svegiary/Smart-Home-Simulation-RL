from models.Devices.AC.AC import AirConditioner
from models.Devices.AC.ACState import OffState
from models.Devices.LightBulb.LightBulb import LightBulb
from models.Home.Home import Home
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
        self.active_acs = []
        self.active_lights = []
        self.active_dehumidifers = []
        self.current_power_consumption = 0

    def active_ac(self):
        active_ac = []
        for room in self.home.rooms.values():
            for key, device in room.devices.items():
                if device.device_type == DeviceType.AC and not isinstance(device.state, OffState):
                    active_ac.append(device)
        self.active_acs = active_ac

    def active_lights(self):
        active_lights = 0
        for key, value in self.home.rooms.items():
            for key, device in value.devices.items():
                if device.device_type == DeviceType.LIGHT:
                    active_lights += 1
        self.active_lights = active_lights

    def count_dehumidifers(self):
        active_dehumidiers = []
        for room in self.home.rooms.values():
            for key, device in room.devices.items():
                if device.device_type == DeviceType.DEHUMIDIFIER:
                    active_dehumidiers.append(device)
        self.active_dehumidifers = active_dehumidiers
