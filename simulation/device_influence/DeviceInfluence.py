from models.Devices.AC.ACState import ACState, OffState
from models.Devices.StateRepresentation.StateRepresentation import RepresentState
from models.Home.Home import Home
from enums.Rooms import HomeRooms
from enums.DeviceType import DeviceType
from simulation.Simulation import Simulation


class DeviceInfluence:

    def __init__(self, sim:  Simulation):
        self.sim = sim
        self.active_acs = 0
        self.active_lights = 0
        self.current_power_consumption = 0

    def active_ac(self):
        active_ac = 0
        for room in self.sim.home.rooms.values():
            print(room.name)
            for key, device in room.devices.items():
                print(device)
                if device.device_type == DeviceType.AC:
                    print("here")

                    if not isinstance(device.state, OffState):
                        print("here")
                        active_ac += 1
                    self.active_acs = active_ac

    def active_lights(self):
        active_lights = 0
        for key, value in self.sim.home.rooms.items():
            print(value)
            for key, device in value.devices.items():
                if device.device_type == DeviceType.LIGHT:
                    active_lights += 1
                    self.active_lights = active_lights
