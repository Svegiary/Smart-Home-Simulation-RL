from enums.MotionSensorEvents import MotionSensorEvent
from models.StateObservation.Subject import Subject


class MotionSensor(Subject):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.motion_detected = False

    def notify(self):
        for observer in self.observers:
            if self.motion_detected == True:
                self.motion_detected = False
                observer.update(MotionSensorEvent.LEAVING)
            else:
                self.motion_detected = True
                observer.update(MotionSensorEvent.COMING)
