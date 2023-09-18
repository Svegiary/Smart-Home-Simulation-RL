from enums.MotionSensorEvents import MotionSensorEvent
from models.Devices.StateObservation.Subject import Subject
from models.Sensors.Sensor import Sensor


class MotionSensor(Subject, Sensor):
    def __init__(self, name):
        super().__init__()
        super(Subject, self).__init__(name)

    def trigger(self):
        self.triggered = not self.triggered
        print(self.triggered)
        self.notify()

    def notify(self):
        for observer in self.observers:
            if self.triggered == True:
                observer.update(MotionSensorEvent.LEAVING)
            else:
                observer.update(MotionSensorEvent.COMING)
