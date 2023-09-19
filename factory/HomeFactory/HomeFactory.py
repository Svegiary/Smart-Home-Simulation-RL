from factory.DeviceFactory.DeviceFactory import DeviceFactory
from enums.Rooms import HomeRooms
from models.Devices.LightBulb.LightBulb import LightBulb
from models.Home.Home import Home
from models.Home.Rooms.Rooms import Room
from models.Sensors.MotionSensor.MotionSensor import MotionSensor
from enums.DeviceType import DeviceType


class HomeFactory:
    def create_home(self):
        living_room = Room(HomeRooms.LIVING_ROOM)
        bedroom_room = Room(HomeRooms.BEDROOM)
        kitchen = Room(HomeRooms.KITCHEN)
        bathroom = Room(HomeRooms.BATHROOM)

        living_room_light = DeviceFactory.create_device(
            DeviceType.LIGHT, "Living Room Light")
        living_room_motion_sensor = MotionSensor("Living Room Motion Sensor")

        bedroom_room_light = DeviceFactory.create_device(
            DeviceType.LIGHT, "Bedroom Light")
        bedroom_room_motion_sensor = MotionSensor("Bedroom Motion Sensor")

        kitchen_light = DeviceFactory.create_device(
            DeviceType.LIGHT, "Kitchen Light")
        kitchen_motion_sensor = MotionSensor("Kitchen Motion Sensor")

        bathroom_light = DeviceFactory.create_device(
            DeviceType.LIGHT, "Bathroom Light")
        bathroom_motion_sensor = MotionSensor("Bathroom Motion Sensor")

        living_room.attach_device(living_room_light)
        living_room.attach_sensor(living_room_motion_sensor)

        bedroom_room.attach_device(bedroom_room_light)
        bedroom_room.attach_sensor(bedroom_room_motion_sensor)

        kitchen.attach_device(kitchen_light)
        kitchen.attach_sensor(kitchen_motion_sensor)

        bathroom.attach_device(bathroom_light)
        bathroom.attach_sensor(bathroom_motion_sensor)

        rooms = [living_room, bedroom_room, kitchen, bathroom]
        return Home(rooms)
