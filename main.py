from models.Devices.LightBulb.LightBulb import LightBulb
from models.Devices.LightBulb.LightBulbSubscriber import LightBulbSubscriber
from models.Sensors.MotionSensor.MotionSensor import MotionSensor
from models.Devices.StateRepresentation.StateRepresentation import RepresentState
from models.Home.HomeRepresentation.PrintSensors import RepresentSensor


BedroomLight = LightBulb("Bedroom Light")
Sensor = MotionSensor("BedroomSensor")
Observer = LightBulbSubscriber(BedroomLight)
Sensor.attach(Observer)
RepresentState.print(BedroomLight)
print(Sensor.triggered)
Sensor.trigger()
RepresentState.print(BedroomLight)

Sensor.trigger()
RepresentState.print(BedroomLight)

Sensor.trigger()
RepresentState.print(BedroomLight)
Sensor.trigger()
RepresentState.print(BedroomLight)
Sensor.trigger()
RepresentState.print(BedroomLight)
RepresentSensor.print(Sensor)
