from enums.Rooms import HomeRooms
from models.Devices.LightBulb.LightBulb import LightBulb
from models.Home.Home import Home
from models.Home.Rooms.Rooms import Room
from models.Sensors.MotionSensor.MotionSensor import MotionSensor


class HomeFactory:
    def create_home(self):
        living_room = Room(HomeRooms.LIVING_ROOM)
        bedroom_room = Room(HomeRooms.BEDROOM)
        kitchen = Room(HomeRooms.KITCHEN)
        bathroom = Room(HomeRooms.BATHROOM)

        living_room_light = LightBulb("Living Room Light")
        living_room_motion_sensor = MotionSensor("Living Room Motion Sensor")

        bedroom_room_light = LightBulb("Bedroom Room Light")
        bedroom_room_motion_sensor = MotionSensor("Bedroom Motion Sensor")

        kitchen_light = LightBulb("Kitchen Light")
        kitchen_motion_sensor = MotionSensor("Kitchen Motion Sensor")

        bathroom_light = LightBulb("Bathroom Light")
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
