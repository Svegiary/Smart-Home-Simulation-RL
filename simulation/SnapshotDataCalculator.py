from models.devices.ac.ac_state import CoolingState, HeatingState
from models.devices.dehumidifier.dehumidifier_state import OffState, OnState
from models.Home.Home import Home
from simulation.home_devices_snapshot.HomeDeviceSnapshot import HomeDeviceSnapshot


class SnapshotDataCalculator:
    def __init__(self, home_device_snapshot: HomeDeviceSnapshot) -> None:
        self.home_device_snapshot = home_device_snapshot
        self.temperature = TemperatureCalculator(self.home_device_snapshot)
        self.humidity = HumidityCalculator(self.home_device_snapshot)

    def calculate_temp(self, outside_temp):
        return self.temperature.calculate_temp(outside_temp)

    def calculate_humidity(self, outside_humidity):
        return self.humidity.calculate_humidity(outside_humidity)

    def calculate_sunlight(self):
        pass


class TemperatureCalculator:
    def __init__(self, home_device_snapshot: HomeDeviceSnapshot) -> None:
        self.home = home_device_snapshot.home
        self.home_device_snapshot = home_device_snapshot

    def outside_temp_infulence(self, inside_temp, outside_temp):
        if inside_temp > outside_temp:
            inside_temp -= round(inside_temp - outside_temp) / 2
        elif inside_temp == outside_temp:
            pass
        else:
            inside_temp += (outside_temp - inside_temp) / 2
        return inside_temp

    def calculate_temp(self, outside_temp):
        if self.home.house_temp == 0:
            self.home.set_house_temp(outside_temp)
            print(self.home.house_temp)
            return outside_temp
        else:
            home_device_snapshot = self.home_device_snapshot
            home_device_snapshot.active_ac()
            for ac in home_device_snapshot.active_acs:
                if isinstance(ac.state, HeatingState):
                    new_temp = self.outside_temp_infulence(
                        self.home.house_temp, outside_temp)
                    self.home.set_house_temp(new_temp + 5)
                    return self.home.house_temp
                elif isinstance(ac.state, CoolingState):
                    new_temp = self.outside_temp_infulence(
                        self.home.house_temp, outside_temp)
                    self.home.set_house_temp(new_temp - 5)
                    return self.home.house_temp

            self.home.set_house_temp(self.outside_temp_infulence(
                self.home.house_temp, outside_temp))
            return self.home.house_temp


class HumidityCalculator:
    def __init__(self, home_device_snapshot: HomeDeviceSnapshot) -> None:
        self.home = home_device_snapshot.home
        self.home_device_snapshot = home_device_snapshot

    def outside_humidity_infulence(self, inside_humidity, outside_humidity):
        if inside_humidity > outside_humidity:
            inside_humidity -= round(inside_humidity - outside_humidity) / 4
        elif inside_humidity == outside_humidity:
            pass
        else:
            inside_humidity += (outside_humidity - inside_humidity) / 4
        return inside_humidity

    def calculate_humidity(self, outside_humidity):
        if self.home.house_humidity == 0:
            self.home.set_house_humidity(outside_humidity)
            return outside_humidity
        else:
            home_device_snapshot = self.home_device_snapshot
            home_device_snapshot.count_dehumidifers()
            for dehumidifier in home_device_snapshot.active_dehumidifers:
                if isinstance(dehumidifier.state, OnState):
                    new_humidity = self.outside_humidity_infulence(
                        self.home.house_humidity, outside_humidity)

                    self.home.set_house_humidity(new_humidity - 10)
                    return self.home.house_humidity
            new_humidity = self.outside_humidity_infulence(
                self.home.house_humidity, outside_humidity)
            self.home.set_house_humidity(new_humidity)
            return self.home.house_humidity
