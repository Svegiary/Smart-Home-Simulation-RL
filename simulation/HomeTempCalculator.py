from models.Devices.AC.ACState import CoolingState, HeatingState
from models.Home.Home import Home
from simulation.device_influence.DeviceInfluence import DeviceInfluence


class HomeTempCalculator:
    def __init__(self, device_influence: DeviceInfluence) -> None:
        self.home = device_influence.home
        self.device_influence = device_influence

    def outside_temp_infulence(self, inside_temp, outside_temp):
        print("inside", inside_temp, "outside", outside_temp)
        if inside_temp > outside_temp:
            print("less")
            inside_temp -= (inside_temp - outside_temp) / 2
        elif inside_temp == outside_temp:
            pass
        else:
            print("omg")
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
                    self.home.set_house_temp(self.house_temp + 0.5)
                    return self.home.house_temp
                elif isinstance(ac.state, CoolingState):
                    self.home.set_house_temp(self.house_temp - 0.5)
                    return self.home.house_temp

            self.home.set_house_temp(self.outside_temp_infulence(
                self.home.house_temp, outside_temp))
            return self.home.house_temp
