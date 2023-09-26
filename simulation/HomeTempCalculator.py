from models.Devices.AC.ACState import CoolingState, HeatingState
from models.Home.Home import Home
from simulation.home_devices_snapshot.HomeDeviceSnapshot import HomeDeviceSnapshot


class HomeTempCalculator:
    def __init__(self, device_influence: HomeDeviceSnapshot) -> None:
        self.home = device_influence.home
        self.device_influence = device_influence

    def outside_temp_infulence(self, inside_temp, outside_temp):
        if inside_temp > outside_temp:
            inside_temp -= round(inside_temp - outside_temp) / 2
        elif inside_temp == outside_temp:
            pass
        else:
            inside_temp += (outside_temp - inside_temp) / 2
        return inside_temp

    def calculate_temp(self, outside_temp):
        print(self.home.house_temp)
        if self.home.house_temp == 0:
            self.home.set_house_temp(outside_temp)
            print(self.home.house_temp)
            return outside_temp
        else:
            device_influence = self.device_influence
            device_influence.active_ac()
            for ac in device_influence.active_acs:
                if isinstance(ac.state, HeatingState):
                    new_temp = self.outside_temp_infulence(
                        self.home.house_temp, outside_temp)
                    self.home.set_house_temp(new_temp + 3)
                    return self.home.house_temp
                elif isinstance(ac.state, CoolingState):
                    new_temp = self.outside_temp_infulence(
                        self.home.house_temp, outside_temp)
                    self.home.set_house_temp(new_temp - 3)
                    return self.home.house_temp

            self.home.set_house_temp(self.outside_temp_infulence(
                self.home.house_temp, outside_temp))
            return self.home.house_temp
