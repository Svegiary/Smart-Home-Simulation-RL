"""
This file contains the classes for determining what the temp and 
humidity will be based on outside variables and device states
"""

from models.devices.ac.ac_state import CoolingState, HeatingState
from models.devices.dehumidifier.dehumidifier_state import OffState, OnState
from simulation.home_devices_snapshot.home_device_snapshot import HomeDeviceSnapshot


class SnapshotDataCalculator:
    """
    Encapsulates the logic for calculating the temperature, humidity, and sunlight(todo)
    """

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
    """
    Calculates the temperature based on the outside temperature and devices
    """

    def __init__(self, home_device_snapshot: HomeDeviceSnapshot) -> None:
        self.home = home_device_snapshot.home
        self.home_device_snapshot = home_device_snapshot

    def outside_temp_infulence(self, inside_temp, outside_temp) -> float:
        """
        Calculates the influence of the outside temperature and the 
        current inside temperature
        """
        if inside_temp > outside_temp:
            inside_temp -= round(inside_temp - outside_temp) / 2
        elif inside_temp == outside_temp:
            pass
        else:
            inside_temp += (outside_temp - inside_temp) / 2
        return inside_temp

    def calculate_temp(self, outside_temp) -> float:
        """
        Calculates the inside temperature based on the outside temperature and the ac
        """
        if self.home.house_temp == 0:  # if temp is 0 , then set same as outside temp
            self.home.set_house_temp(outside_temp)
            print(self.home.house_temp)
            return outside_temp
        else:
            home_device_snapshot = self.home_device_snapshot
            home_device_snapshot.count_ac()
            for ac in home_device_snapshot.active_acs:  # we now have 1 ac , but if we had 2 , we  have to drop by 10c
                if isinstance(ac.state, HeatingState):  # if it is in heating mode
                    new_temp = self.outside_temp_infulence(  # calculate outside temp influence
                        self.home.house_temp, outside_temp)
                    # reaise temp by 5 on top of the new temp
                    # set new internal temp
                    self.home.set_house_temp(new_temp + 5)
                    return self.home.house_temp
                elif isinstance(ac.state, CoolingState):  # if it is in cooling mode
                    new_temp = self.outside_temp_infulence(  # calculate outside temp influence
                        self.home.house_temp, outside_temp)
                    # drop temp by 5 on top of the new temp
                    # set new internal temp
                    self.home.set_house_temp(new_temp - 5)
                    return self.home.house_temp

            self.home.set_house_temp(self.outside_temp_infulence(
                self.home.house_temp, outside_temp))
            return self.home.house_temp


class HumidityCalculator:
    """
    Calculates the humidity based on the outside humidity and devices
    """

    def __init__(self, home_device_snapshot: HomeDeviceSnapshot) -> None:
        self.home = home_device_snapshot.home
        self.home_device_snapshot = home_device_snapshot

    def outside_humidity_infulence(self, inside_humidity, outside_humidity) -> float:
        """
        Calculates the influence of the outside humidity and the 
        current inside humidity
        """
        if inside_humidity > outside_humidity:
            inside_humidity -= round(inside_humidity - outside_humidity) / 4
        elif inside_humidity == outside_humidity:
            pass
        else:
            inside_humidity += (outside_humidity - inside_humidity) / 4
        return inside_humidity

    def calculate_humidity(self, outside_humidity) -> float:
        """
        Calculates the inside humidity based on the outside humidity and the dehumidifier
        """
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
