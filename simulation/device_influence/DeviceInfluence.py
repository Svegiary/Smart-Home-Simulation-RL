from models.Devices.AC.AC import AirConditioner
from models.Devices.AC.ACState import ACState, OffState
from models.Devices.LightBulb.LightBulb import LightBulb
from models.Devices.StateRepresentation.StateRepresentation import RepresentState
from models.Home.Home import Home
from enums.Rooms import HomeRooms
from enums.DeviceType import DeviceType


class DeviceInfluence:

    def __init__(self, home:  Home):
        self.home = home
        self.active_acs: list[AirConditioner] = []
        self.active_lights: list[LightBulb] = []
        self.current_power_consumption = 0

    def active_ac(self):
        active_ac = []
        for room in self.home.rooms.values():
            for key, device in room.devices.items():
                if device.device_type == DeviceType.AC:

                    if not isinstance(device.state, OffState):
                        active_ac.append(device)
                    self.active_acs = active_ac

    def active_lights(self):
        active_lights = 0
        for key, value in self.home.rooms.items():
            for key, device in value.devices.items():
                if device.device_type == DeviceType.LIGHT:
                    active_lights += 1
                    self.active_lights = active_lights
