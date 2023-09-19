from enums.Rooms import HomeRooms
from factory.HomeFactory.HomeFactory import HomeFactory
from models.Devices.LightBulb.LightBulb import LightBulb
from models.Devices.LightBulb.LightBulbSubscriber import LightBulbSubscriber
from models.Home.HomeRepresentation.PrintHome import PrintHome
from models.Sensors.MotionSensor.MotionSensor import MotionSensor
from models.Devices.StateRepresentation.StateRepresentation import RepresentState
from models.Home.HomeRepresentation.PrintSensors import RepresentSensor
from models.Home.HomeController import HomeController
from enums.DeviceType import DeviceType

home = HomeFactory().create_home()
print(home.rooms)

PrintHome.print(home)

home_controller = HomeController(home)

home_controller.turn_on_device(HomeRooms.LIVING_ROOM, DeviceType.LIGHT)
PrintHome.print(home)

home_controller.turn_off_device(HomeRooms.LIVING_ROOM, DeviceType.LIGHT)
PrintHome.print(home)
