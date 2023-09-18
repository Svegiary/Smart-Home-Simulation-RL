from factory.HomeFactory.HomeFactory import HomeFactory
from models.Devices.LightBulb.LightBulb import LightBulb
from models.Devices.LightBulb.LightBulbSubscriber import LightBulbSubscriber
from models.Home.HomeRepresentation.PrintHome import PrintHome
from models.Sensors.MotionSensor.MotionSensor import MotionSensor
from models.Devices.StateRepresentation.StateRepresentation import RepresentState
from models.Home.HomeRepresentation.PrintSensors import RepresentSensor


home = HomeFactory().create_home()
print(home.rooms)

PrintHome.print(home)
