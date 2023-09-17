from enums.MotionSensorEvents import MotionSensorEvent
from models.StateObservation.Subject import Subject


class MotionSensor(Subject):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.motion_detected = False

    def trigger(self):
        self.motion_detected = not self.motion_detected
        print(self.motion_detected)
        self.notify()

    def notify(self):
        for observer in self.observers:
            if self.motion_detected == True:
                observer.update(MotionSensorEvent.LEAVING)
            else:
                observer.update(MotionSensorEvent.COMING)
