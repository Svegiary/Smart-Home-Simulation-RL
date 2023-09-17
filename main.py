from models.LightBulb.LightBulb import LightBulb
from models.LightBulb.LightBulbSubscriber import LightBulbSubscriber
from models.MotionSensor.MotionSensor import MotionSensor
from models.StateRepresentation.StateRepresentation import RepresentState


BedroomLight = LightBulb("Bedroom Light")
Sensor = MotionSensor("BedRoom Sensor")
Observer = LightBulbSubscriber(BedroomLight)
Sensor.attach(Observer)
RepresentState.print(BedroomLight)
print(Sensor.motion_detected)
Sensor.motion_detected = True
Sensor.notify()
RepresentState.print(BedroomLight)

Sensor.notify()
RepresentState.print(BedroomLight)
