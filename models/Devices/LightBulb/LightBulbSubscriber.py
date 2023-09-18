from enums.MotionSensorEvents import MotionSensorEvent
from models.Devices.LightBulb.LightBulb import LightBulb
from models.Devices.StateObservation.Observer import Observer


class LightBulbSubscriber(Observer):
    def __init__(self, light_bulb: LightBulb):
        self.light_bulb = light_bulb

    def update(self, event: MotionSensorEvent):
        if (event is MotionSensorEvent.LEAVING):
            self.light_bulb.turn_off()
        else:
            self.light_bulb.turn_on()
