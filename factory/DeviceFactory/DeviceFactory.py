from models.Devices.LightBulb.LightBulb import LightBulb
from enums.DeviceType import DeviceType
from models.Devices.LightBulb.LightBulbController import LightBulbController


class DeviceFactory:

    @staticmethod
    def create_device(device_type, name):
        if device_type == DeviceType.LIGHT:
            return LightBulb(name, LightBulbController())
