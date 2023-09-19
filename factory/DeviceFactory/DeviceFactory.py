from models.Devices.AC.AC_Controller import AcController
from models.Devices.LightBulb.LightBulb import LightBulb
from enums.DeviceType import DeviceType
from models.Devices.LightBulb.LightBulbController import LightBulbController
from models.Devices.AC.AC import AirConditioner


class DeviceFactory:

    @staticmethod
    def create_device(device_type, name):
        if device_type == DeviceType.LIGHT:
            return LightBulb(name, LightBulbController())
        if device_type == DeviceType.AC:
            return AirConditioner(name, AcController())
