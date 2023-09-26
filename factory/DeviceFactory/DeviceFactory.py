from models.Devices.Dehumidifier.Dehumidifier import Dehumidifier
from models.Devices.LightBulb.LightBulb import LightBulb
from enums.DeviceType import DeviceType
from models.Devices.AC.AC import AirConditioner


class DeviceFactory:

    @staticmethod
    def create_device(device_type, name, power_consumption):
        if device_type == DeviceType.LIGHT:
            return LightBulb(name, power_consumption)
        elif device_type == DeviceType.AC:
            return AirConditioner(name, power_consumption)
        elif device_type == DeviceType.DEHUMIDIFIER:
            return Dehumidifier(name, power_consumption)
