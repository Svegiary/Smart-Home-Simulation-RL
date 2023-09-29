"""
-home_factory.py
This file contains the logic for creating the home and attaching devices
and sensors

The current implementation consists of four rooms
Each room has a light bulb and a motion sensor

The living room also has an ac and a dehumidifier that control 
the temp and humidity of the whole house , for simplicity's sake
"""

from factory.device_factory.device_factory import DeviceFactory
from enums.Rooms import HomeRooms
from models.home.home import Home
from models.home.rooms.rooms import Room
from models.Sensors.MotionSensor.MotionSensor import MotionSensor
from enums.DeviceType import DeviceType


class HomeFactory:

    @staticmethod
    def create_home() -> Home:
        """
        Create a home that has 4 rooms , a light in each room. The living room also has an ac and dehumidifier
        """
        living_room = Room(HomeRooms.LIVING_ROOM)
        bedroom_room = Room(HomeRooms.BEDROOM)
        kitchen = Room(HomeRooms.KITCHEN)
        bathroom = Room(HomeRooms.BATHROOM)

        living_room_ac = DeviceFactory.create_device(
            DeviceType.AC, "Living Room AC", 2000
        )

        living_room_dehumidifier = DeviceFactory.create_device(
            DeviceType.DEHUMIDIFIER, "Living Room Dehumidifier", 500)

        living_room_light = DeviceFactory.create_device(
            DeviceType.LIGHT, "Living Room Light", 5)
        living_room_motion_sensor = MotionSensor("Living Room Motion Sensor")

        bedroom_room_light = DeviceFactory.create_device(
            DeviceType.LIGHT, "Bedroom Light", 5)
        bedroom_room_motion_sensor = MotionSensor("Bedroom Motion Sensor")

        kitchen_light = DeviceFactory.create_device(
            DeviceType.LIGHT, "Kitchen Light", 5)
        kitchen_motion_sensor = MotionSensor("Kitchen Motion Sensor")

        bathroom_light = DeviceFactory.create_device(
            DeviceType.LIGHT, "Bathroom Light", 5)
        bathroom_motion_sensor = MotionSensor("Bathroom Motion Sensor")

        living_room.attach_device(living_room_light)
        living_room.attach_device(living_room_dehumidifier)
        living_room.attach_device(living_room_ac)
        living_room.attach_sensor(living_room_motion_sensor)

        bedroom_room.attach_device(bedroom_room_light)
        bedroom_room.attach_sensor(bedroom_room_motion_sensor)

        kitchen.attach_device(kitchen_light)
        kitchen.attach_sensor(kitchen_motion_sensor)

        bathroom.attach_device(bathroom_light)
        bathroom.attach_sensor(bathroom_motion_sensor)

        rooms = [living_room, bedroom_room, kitchen, bathroom]
        return Home(rooms)
