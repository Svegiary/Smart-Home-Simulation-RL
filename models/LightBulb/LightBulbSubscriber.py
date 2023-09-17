from enums.MotionSensorEvents import MotionSensorEvent
from models.LightBulb.LightBulb import LightBulb
from models.StateObservation.Observer import Observer


class LightBulbSubscriber(Observer):
    def __init__(self, light_bulb: LightBulb):
        self.light_bulb = light_bulb

    def update(self, event):
        if (event is MotionSensorEvent.LEAVING):
            self.light_bulb.turn_off()
        else:
            self.light_bulb.turn_on()
