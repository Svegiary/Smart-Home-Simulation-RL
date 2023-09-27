from enums.DeviceType import DeviceType
from enums.Rooms import HomeRooms
from factory.CommandFactory.CommandFactory import CommandFactory
from factory.HomeFactory.HomeFactory import HomeFactory
from models.Command.ACCommands import *
from models.Command.Invoker import Invoker
from representation.HomeRepresentation.PrintHome import PrintHome
from simulation.Simulation import Simulation
from simulation.SimulationController import SimulationController
from simulation.config.simulation_config import SimulationConfig
from simulation.data_generation.data_factories.humidity_factory import HumidityFactory
from simulation.data_generation.data_factories.sunlight_factory import SunlightFactory
from simulation.data_generation.data_factories.temperature_factory import TemperatureFactory
from simulation.data_generation.simulation_data_factory import SimulationDataFactory
from simulation.data_generation.timestamp_generation.timestamp import TimestampGeneration
from simulation.SimulationRuntime import *

config = SimulationConfig()
constraints = {
    "max_temp": 30,
    "min_temp": 10,
    "max_humidity": 100,
    "min_humidity": 0,
}

config.set_constraints(constraints)

simulation_params = {
    "time_interval": 10,  # minutes
    "simulation_duration": 24
}
config.set_simulation_params(simulation_params)

timestamps = TimestampGeneration(config)
timestamps.generate_timestamps()

temp_factory = TemperatureFactory(config, timestamps)
humidity_factory = HumidityFactory(config, timestamps)
sunlight_factory = SunlightFactory(config, timestamps)

data = SimulationDataFactory.create_simulation_data(
    temp_factory, humidity_factory, sunlight_factory)

print(data.temp_data)
print(data.sunlight_data)
print(data.humidity_data)

home = HomeFactory().create_home()

PrintHome.print(home)
command_Factory = CommandFactory(home)
command_Factory.create_commands()

home.place_human(HomeRooms.LIVING_ROOM)

sim = Simulation(
    timestamps,
    data,
    home,
    SimulationController(command_Factory.commands,
                         Invoker()
                         ),
    config
)
print("setting runtime")

sim.set_runtime_plan(DefaultRuntime())
print(timestamps)
print("starting runtime //////////////////////////////////////////////////////////////////////////////////")
sim.start()
print("finished runtime //////////////////////////////////////////////////////////////////////////////////")

import os

# Specify the directory of your Python project.
project_directory = '/home/harry/Documents/ai2cyber/'

# Specify the output file where the concatenated content will be saved.
output_file = 'concatenated_code.py'

# Function to concatenate the contents of all Python files in a directory.


def concatenate_python_files(directory, output_file):
    with open(output_file, 'w') as output:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as input_file:
                        output.write(input_file.read())
                        # Add a newline separator between files
                        output.write('\n')


# Concatenate Python files in the specified project directory.
concatenate_python_files(project_directory, output_file)

print(f'Concatenated code saved to {output_file}')



from models.Home.Rooms.Rooms import Room
from simulation.SnapshotDataCalculator import SnapshotDataCalculator
from simulation.human.Human import Human


class SimulationSnapshot:
    def __init__(self, outside_temp, outside_humidity, human:  Human, calculator: SnapshotDataCalculator):
        self.outside_temp = outside_temp
        self.outside_humidity = outside_humidity
        self.inside_temp = calculator.calculate_temp(outside_temp)
        self.inside_humidity = calculator.calculate_humidity(outside_humidity)

        self.human_location = human.human_location

    def print(self):
        print("//////////////////////////////////////////////")
        print("Outside temp : ", self.outside_temp,
              "| Inside temp : ", self.inside_temp)
        print("-----------------------------------------------")
        print("Outside humidity : ", self.outside_humidity,
              "| Inside humidity : ", self.inside_humidity)
        print("-----------------------------------------------")
        print("Human location : ", self.human_location.name)
        print("-----------------------------------------------")


class SnapshotEvaluation:
    pass

from abc import abstractmethod, ABC
from time import sleep
from enums.Rooms import HomeRooms
from models.Command.Invoker import Invoker

from simulation.SimulationSnapshot import SimulationSnapshot


class SimulationRuntime(ABC):
    def __init__(self):
        self.snapshots: list[SimulationSnapshot] = []
        self.invoker = Invoker()  # TODO: hell no

    @abstractmethod
    def start(self, sim):
        pass


class NoRuntime(SimulationRuntime):
    def start(self, sim):
        print("Please set runtime plan")


class DefaultRuntime(SimulationRuntime):
    def start(self, sim):
        for timestamp in sim.timestamps:
            snapshot = sim.extract_snapshot(timestamp)
            self.snapshots.append(snapshot)
            snapshot.print()
            sleep(0.1)


class CallToActionRuntime(SimulationRuntime):
    def start(self, sim):
        for timestamp in sim.timestamps:
            snapshot = sim.extract_snapshot(timestamp)
            self.snapshots.append(snapshot)
            snapshot.print()
            execute = input("Choose Action")
            sleep(0.1)


class ControllerAcRuntime(SimulationRuntime):
    def start(self, sim):
        for timestamp in sim.timestamps:
            snapshot = sim.extract_snapshot(timestamp)
            self.snapshots.append(snapshot)
            snapshot.print()
            print("Actions")
            print("1) Set cooling")
            print("2) Set Heating")
            print("3) Turn off")
            print("4) Do nothing")
            while True:
                command = input("Option:")
                if command == "1":

                    sim.controller.set_cooling()
                    break
                elif command == "2":

                    sim.controller.set_heating()
                    break
                elif command == "3":
                    sim.controller.turn_off_ac()
                    break
                elif command == "4":
                    print("doing nothing")
                    break
                else:
                    print("invalid action")
                    continue
            print("------------------------------------")


class ControllerDehumidifierRuntime(SimulationRuntime):
    def start(self, sim):
        for timestamp in sim.timestamps:
            snapshot = sim.extract_snapshot(timestamp)
            self.snapshots.append(snapshot)
            snapshot.print()
            print("Actions")
            print("1) Turn off")
            print("2) Turn on")
            print("3) Do nothing")
            while True:
                command = input("Option:")
                if command == "1":

                    sim.controller.turn_off_dehumidifier()
                    break
                elif command == "2":

                    sim.controller.turn_on_dehumidifier()
                    break
                elif command == "3":
                    break

                else:
                    print("invalid action")
                    continue
            print("------------------------------------")


class HumanMovementRuntime(SimulationRuntime):
    def start(self, sim):
        for timestamp in sim.timestamps:
            snapshot = sim.extract_snapshot(timestamp)
            self.snapshots.append(snapshot)
            snapshot.print()
            print("Actions")
            print("1) Move human to living room")
            print("2) Move human to bedroom")
            print("3) Move human to bathroom")
            print("4) Move human to kitchen")
            print("5) Dont move")
            while True:
                command = input("Option:")
                if command == "1":

                    sim.home.place_human(HomeRooms.LIVING_ROOM)
                    break
                elif command == "2":

                    sim.home.place_human(HomeRooms.BEDROOM)
                    break
                elif command == "3":
                    sim.home.place_human(HomeRooms.BATHROOM)
                    break
                elif command == "4":
                    sim.home.place_human(HomeRooms.KITCHEN)
                    break
                elif command == "5":
                    break
                else:
                    print("invalid action")
                    continue
            print("------------------------------------")

from models.Devices.AC.ACState import CoolingState, HeatingState
from models.Devices.Dehumidifier.DehumidifierSate import OffState, OnState
from models.Home.Home import Home
from simulation.home_devices_snapshot.HomeDeviceSnapshot import HomeDeviceSnapshot


class SnapshotDataCalculator:
    def __init__(self, home_device_snapshot: HomeDeviceSnapshot) -> None:
        self.home_device_snapshot = home_device_snapshot
        self.temperature = TemperatureCalculator(self.home_device_snapshot)
        self.humidity = HumidityCalculator(self.home_device_snapshot)

    def calculate_temp(self, outside_temp):
        return self.temperature.calculate_temp(outside_temp)

    def calculate_humidity(self, outside_humidity):
        return self.humidity.calculate_humidity(outside_humidity)

    def calculate_sunlight(self):
        pass


class TemperatureCalculator:
    def __init__(self, home_device_snapshot: HomeDeviceSnapshot) -> None:
        self.home = home_device_snapshot.home
        self.home_device_snapshot = home_device_snapshot

    def outside_temp_infulence(self, inside_temp, outside_temp):
        if inside_temp > outside_temp:
            inside_temp -= round(inside_temp - outside_temp) / 2
        elif inside_temp == outside_temp:
            pass
        else:
            inside_temp += (outside_temp - inside_temp) / 2
        return inside_temp

    def calculate_temp(self, outside_temp):
        if self.home.house_temp == 0:
            self.home.set_house_temp(outside_temp)
            print(self.home.house_temp)
            return outside_temp
        else:
            home_device_snapshot = self.home_device_snapshot
            home_device_snapshot.active_ac()
            for ac in home_device_snapshot.active_acs:
                if isinstance(ac.state, HeatingState):
                    new_temp = self.outside_temp_infulence(
                        self.home.house_temp, outside_temp)
                    self.home.set_house_temp(new_temp + 5)
                    return self.home.house_temp
                elif isinstance(ac.state, CoolingState):
                    new_temp = self.outside_temp_infulence(
                        self.home.house_temp, outside_temp)
                    self.home.set_house_temp(new_temp - 5)
                    return self.home.house_temp

            self.home.set_house_temp(self.outside_temp_infulence(
                self.home.house_temp, outside_temp))
            return self.home.house_temp


class HumidityCalculator:
    def __init__(self, home_device_snapshot: HomeDeviceSnapshot) -> None:
        self.home = home_device_snapshot.home
        self.home_device_snapshot = home_device_snapshot

    def outside_humidity_infulence(self, inside_humidity, outside_humidity):
        if inside_humidity > outside_humidity:
            inside_humidity -= round(inside_humidity - outside_humidity) / 4
        elif inside_humidity == outside_humidity:
            pass
        else:
            inside_humidity += (outside_humidity - inside_humidity) / 4
        return inside_humidity

    def calculate_humidity(self, outside_humidity):
        if self.home.house_humidity == 0:
            self.home.set_house_humidity(outside_humidity)
            return outside_humidity
        else:
            home_device_snapshot = self.home_device_snapshot
            home_device_snapshot.count_dehumidifers()
            for dehumidifier in home_device_snapshot.active_dehumidifers:
                if isinstance(dehumidifier.state, OnState):
                    new_humidity = self.outside_humidity_infulence(
                        self.home.house_humidity, outside_humidity)

                    self.home.set_house_humidity(new_humidity - 10)
                    return self.home.house_humidity
            new_humidity = self.outside_humidity_infulence(
                self.home.house_humidity, outside_humidity)
            self.home.set_house_humidity(new_humidity)
            return self.home.house_humidity

from factory.CommandFactory.DehumidifierCommandFactory import DehumidifierCommandFactory
from models.Command.ACCommands import *
from models.Command.DehumidifierCommands import TurnOffDehumidifier, TurnOnDehumidifier
from models.Command.DeviceCommand import DeviceCommand
from models.Command.Invoker import Invoker


class SimulationController:
    def __init__(self, commands: list[DeviceCommand], invoker: Invoker):
        self.commands = commands
        self.invoker = invoker

    def set_heating(self):
        for command in self.commands:
            if isinstance(command, ACSetHeatingCommand):
                self.execute(command)

    def set_cooling(self):
        for command in self.commands:
            if isinstance(command, ACSetCoolingCommand):
                self.execute(command)

    def turn_off_ac(self):
        for command in self.commands:
            if isinstance(command, ACTurnOffCommand):
                self.execute(command)

    def turn_on_dehumidifier(self):
        for command in self.commands:
            if isinstance(command, TurnOnDehumidifier):
                self.execute(command)

    def turn_off_dehumidifier(self):
        for command in self.commands:
            if isinstance(command, TurnOffDehumidifier):
                self.execute(command)

    def execute(self, command):
        self.invoker.execute(command)

from models.Home.Home import Home
from simulation.SnapshotDataCalculator import SnapshotDataCalculator
from simulation.SimulationController import SimulationController
from simulation.config.simulation_config import SimulationConfig
from simulation.data_generation.simulation_data import SimulationData
from simulation.data_generation.timestamp_generation.timestamp import TimestampGeneration
from simulation.SimulationRuntime import *
from simulation.home_devices_snapshot.HomeDeviceSnapshot import HomeDeviceSnapshot


class Simulation:
    def __init__(
            self,
            timestamps: TimestampGeneration,
            simulation_data:  SimulationData,
            home: Home,
            controller: SimulationController,
            config: SimulationConfig,
    ):
        self.timestamps = timestamps.timestamps
        self.simulation_data = simulation_data
        self.home = home
        self.simulation_runtime_plan = NoRuntime()
        self.controller = controller
        self.config = config

    def set_runtime_plan(self, runtime_plan: SimulationRuntime):
        self.simulation_runtime_plan = runtime_plan

    def start(self):
        self.simulation_runtime_plan.start(self)

    def extract_snapshot(self, timestamp):
        return SimulationSnapshot(
            self.simulation_data.temp_data[timestamp],
            self.simulation_data.humidity_data[timestamp],
            self.home.human,
            SnapshotDataCalculator(HomeDeviceSnapshot(self.home))

        )


# simulation has states .
# evaluation based on preferences


class SnapshotGeneration:
    def __init__(self, device_influence):
        pass

    def calculate_temp(self, sim: Simulation):
        pass

from models.Devices.AC.AC import AirConditioner
from models.Devices.AC.ACState import OffState
from models.Devices.LightBulb.LightBulb import LightBulb
from models.Home.Home import Home
from enums.DeviceType import DeviceType


class HomeDeviceSnapshot:
    _instance = None

    def __new__(cls, home: Home):
        if cls._instance is None:
            cls._instance = super(HomeDeviceSnapshot, cls).__new__(cls)
            cls._instance.initialize(home)
        return cls._instance

    def initialize(self, home: Home):
        self.home = home
        self.active_acs = []
        self.active_lights = []
        self.active_dehumidifers = []
        self.current_power_consumption = 0

    def active_ac(self):
        active_ac = []
        for room in self.home.rooms.values():
            for key, device in room.devices.items():
                if device.device_type == DeviceType.AC and not isinstance(device.state, OffState):
                    active_ac.append(device)
        self.active_acs = active_ac

    def active_lights(self):
        active_lights = 0
        for key, value in self.home.rooms.items():
            for key, device in value.devices.items():
                if device.device_type == DeviceType.LIGHT:
                    active_lights += 1
        self.active_lights = active_lights

    def count_dehumidifers(self):
        active_dehumidiers = []
        for room in self.home.rooms.values():
            for key, device in room.devices.items():
                if device.device_type == DeviceType.DEHUMIDIFIER:
                    active_dehumidiers.append(device)
        self.active_dehumidifers = active_dehumidiers

class SimulationConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SimulationConfig, cls).__new__(cls)
            cls._instance.initialize_config()
        return cls._instance

    def initialize_config(self):
        self.time_interval = None
        self.simulation_duration = None
        self.max_temp = None
        self.min_temp = None
        self.max_humidity = None
        self.min_humidity = None

    def set_constraints(self, constraints):
        self.max_temp = constraints["max_temp"]
        self.min_temp = constraints["min_temp"]
        self.max_humidity = constraints["max_humidity"]
        self.min_humidity = constraints["min_humidity"]

    def set_simulation_params(self, simulation_params):
        self.time_interval = simulation_params["time_interval"]
        self.simulation_duration = simulation_params["simulation_duration"]

from typing import Dict


class Preferences:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Preferences, cls).__new__(cls)
            cls._instance.initialize_preferences()
        return cls._instance

    def initialize_preferences(self):
        self.target_temp = None
        self.target_hum = None
        self.target_luminance = None
        self.target_noise = None

    def set_preferences(self, preferences: Dict):
        self.target_temp = preferences["target_temp"]
        self.target_hum = preferences["target_humidity"]
        self.target_luminance = preferences["target_luminance"]
        self.target_noise = preferences["target_noise"]

from simulation.Simulation import Simulation
from simulation.config.simulation_config import SimulationConfig
from simulation.data_generation.data_factories.temperature_factory import TemperatureFactory
from simulation.data_generation.simulation_data import SimulationData
from simulation.data_generation.simulation_data_factory import SimulationDataFactory
from simulation.data_generation.timestamp_generation.timestamp import TimestampGeneration


class SimulationFactory:

    def __init__(self, config: SimulationConfig):
        self.config = config

    def create_simulation(self):
        timestamps = TimestampGeneration(self.config)
        temp = TemperatureFactory(self.config, timestamps)
        data = SimulationDataFactory.create_simulation_data(temp, 0, 0)
        return Simulation(timestamps, data)

from models.Home.Rooms.Rooms import Room


class Human:
    def __init__(self):
        self.human_location: Room = None

    def place_human(self, room: Room):
        room.place_human()
        if self.human_location is not None:
            self.human_location.remove_human()
            self.human_location = room
        else:
            self.human_location = room

from simulation.data_generation.data_factories.humidity_factory import HumidityFactory
from simulation.data_generation.data_factories.sunlight_factory import SunlightFactory
from simulation.data_generation.data_factories.temperature_factory import TemperatureFactory
from simulation.data_generation.simulation_data import SimulationData


class SimulationDataFactory:
    @staticmethod
    def create_simulation_data(temp_factory: TemperatureFactory, humidity_factory: HumidityFactory, sunlight_factory: SunlightFactory):  # add types
        temp_factory.generateData()

        t = temp_factory.data
        humidity_factory.generateData()

        h = humidity_factory.data

        sunlight_factory.generateData()
        s = sunlight_factory.data

        return SimulationData(t, h, s)

class SimulationData:
    def __init__(self, temp_data, humidity_data, sunlight_data):  # TODO: add types
        self.temp_data = temp_data
        self.humidity_data = humidity_data
        self.sunlight_data = sunlight_data

from simulation.config.simulation_config import SimulationConfig


class SunlightCalculation:
    @staticmethod
    def generate_sunlight(index, duration_hours, config: SimulationConfig):

        no_timestamps = duration_hours / (config.time_interval / 60)
        print("STEPS ", no_timestamps)
        if index < no_timestamps // 2:
            sunlight = (index / (no_timestamps // 2))
            print("SUNLIGHT IS ", sunlight)
        else:
            sunlight = 2.0 - (index / (no_timestamps // 2))
            print("SUNLIGHT IS ", sunlight)
        return round(sunlight, 2)

from simulation.config.simulation_config import SimulationConfig


class TemperatureCalculation:

    @staticmethod
    def generate_temperature(index: int, duration_hours: int, config: SimulationConfig) -> float:
        """
        Generates a temperature value based on the index of the timestamp.

        Args:
            index (int): Index of the timestamp.
            duration_hours (int): Duration of the simulation in hours.
            config (SimulationConfig): Configuration of the simulation.

        Returns:
            float: Temperature value.
        """
        # Calculate the total number of timestamps in the simulation.
        no_timestamps = duration_hours / (config.time_interval / 60)

        if index < no_timestamps / 2:
            # In the first half, temperature rises from min_temp to max_temp linearly.
            temperature = config.min_temp + \
                (index / (no_timestamps / 2)) * \
                (config.max_temp - config.min_temp)
        else:
            # In the second half, temperature decreases from max_temp to min_temp linearly.
            temperature = config.max_temp - \
                ((index - (no_timestamps / 2)) / (no_timestamps / 2)) * \
                (config.max_temp - config.min_temp)

        return round(temperature, 1)

from simulation.config.simulation_config import SimulationConfig


class HumidityCalculation:

    @staticmethod
    def generate_humidity(index: int, duration_hours: float, config: SimulationConfig) -> float:
        """
        Generates a humidity value based on the index of the timestamp.

        Args:
            index (int): Index of the timestamp.
            duration_hours (float): Duration of the simulation in hours.
            config (SimulationConfig): Configuration of the simulation.

        Returns:
            float: Humidity value.
        """
        # Calculate the total number of timestamps in the simulation.
        no_timestamps = duration_hours / (config.time_interval / 60)

        if index < no_timestamps / 2:
            # In the first half, humidity rises from min_humidity to max_humidity linearly.
            humidity = config.min_humidity + \
                (index / (no_timestamps / 2)) * \
                (config.max_humidity - config.min_humidity)
        else:
            # In the second half, humidity decreases from max_humidity to min_humidity linearly.
            humidity = config.max_humidity - \
                ((index - (no_timestamps / 2)) / (no_timestamps / 2)) * \
                (config.max_humidity - config.min_humidity)

        return round(humidity, 1)

import time
from simulation.config.simulation_config import SimulationConfig


class TimestampGeneration:
    _instance = None

    def __new__(cls, config: SimulationConfig):
        if cls._instance is None:
            cls._instance = super(TimestampGeneration, cls).__new__(cls)
            cls._instance.initialize(config)
        return cls._instance

    def initialize(self, config: SimulationConfig):
        self.config = config
        self.current_time = int(time.time())
        self.end_time = self.current_time + config.simulation_duration * 3600
        self.timestamps = []

    def generate_timestamps(self):
        starting_time = self.current_time
        end_time = self.end_time
        while starting_time < end_time:
            self.timestamps.append(starting_time)
            starting_time += self.config.time_interval * 60

from simulation.config.simulation_config import SimulationConfig
from simulation.data_generation.data_calculation.calculate_humidity import HumidityCalculation
from simulation.data_generation.data_factories.data_factory_interface import DataFactory
from simulation.data_generation.timestamp_generation.timestamp import TimestampGeneration


class HumidityFactory(DataFactory):
    def __init__(self, config: SimulationConfig, timestamps: TimestampGeneration):
        super().__init__(config, timestamps)

    def generateData(self):

        for index, timestamp in enumerate(self.timestamps.timestamps):
            value = HumidityCalculation.generate_humidity(
                index, self.config.simulation_duration, self.config)
            self.data[timestamp] = value

from abc import ABC, abstractmethod

from simulation.config.simulation_config import SimulationConfig
from simulation.data_generation.timestamp_generation.timestamp import TimestampGeneration


class DataFactory(ABC):
    def __init__(self, config: SimulationConfig, timestamps: TimestampGeneration):
        self.config = config
        self.current_time = timestamps.current_time
        self.end_time = timestamps.end_time
        self.timestamps = timestamps
        self.data = {}

    @abstractmethod
    def generateData(self):
        pass

from simulation.config.simulation_config import SimulationConfig
from simulation.data_generation.data_calculation.calculate_sunlight import SunlightCalculation
from simulation.data_generation.data_factories.data_factory_interface import DataFactory
from simulation.data_generation.timestamp_generation.timestamp import TimestampGeneration


class SunlightFactory(DataFactory):
    def __init__(self, config: SimulationConfig, timestamps: TimestampGeneration):
        super().__init__(config, timestamps)

    def generateData(self):

        for index, timestamp in enumerate(self.timestamps.timestamps):
            value = SunlightCalculation.generate_sunlight(
                index, self.config.simulation_duration, self.config)
            self.data[timestamp] = value


from simulation.config.simulation_config import SimulationConfig
from simulation.data_generation.data_calculation.calculate_temp import TemperatureCalculation
from simulation.data_generation.data_factories.data_factory_interface import DataFactory
from simulation.data_generation.timestamp_generation.timestamp import TimestampGeneration


class TemperatureFactory(DataFactory):
    def __init__(self, config: SimulationConfig, timestamps: TimestampGeneration):
        super().__init__(config, timestamps)

    def generateData(self):

        for index, timestamp in enumerate(self.timestamps.timestamps):
            value = TemperatureCalculation.generate_temperature(
                index, self.config.simulation_duration, self.config)
            self.data[timestamp] = value

from collections import OrderedDict
from models.Sensors.Sensor import Sensor


class RepresentSensor:

    @staticmethod
    def print(sensor: Sensor):
        ordered_attributes = OrderedDict()
        ordered_attributes["Name"] = sensor.name
        ordered_attributes.update(vars(sensor))

        print("------------------------------")
        for attr_name, attr_value in ordered_attributes.items():
            print(f"{attr_name}: {attr_value}")

        print("------------------------------")

from models.Devices.Device import Device
from collections import OrderedDict


class RepresentState:

    @staticmethod
    def print(device: Device):
        ordered_attributes = OrderedDict()
        ordered_attributes["Name"] = device.name
        ordered_attributes["State"] = device.state
        ordered_attributes.update(vars(device.state))

        print("------------------------------")
        for attr_name, attr_value in ordered_attributes.items():
            print(f"{attr_name}: {attr_value}")

        print("------------------------------")

from typing import List

from representation.SensorRepresenation.RepresentSensor import RepresentSensor
from models.Sensors.Sensor import Sensor


class PrintSensors:

    @staticmethod
    def print(sensors: List[Sensor]):
        for sensor in sensors:
            RepresentSensor.print(sensor)

from typing import Dict, List

from models.Devices.Device import Device
from enums.DeviceType import DeviceType
from representation.StateRepresentation.StateRepresentation import RepresentState


class PrintDevices:

    @staticmethod
    def print(devices: Dict[DeviceType, Device]):
        print(devices.items())
        for device_type, device in devices.items():
            RepresentState.print(device)

from models.Home.Home import Home
from representation.HomeRepresentation.PrintDevices import PrintDevices
from representation.HomeRepresentation.PrintSensors import PrintSensors

from representation.SensorRepresenation.RepresentSensor import RepresentSensor


class PrintHome:
    @staticmethod
    def print(home: Home):
        print("###############################################################")

        for room_name, room_instance in home.rooms.items():
            print(room_name, " : ")
            PrintDevices.print(room_instance.devices)
            PrintSensors.print(room_instance.sensors)
        print("###############################################################")

from enum import Enum


class DeviceType(Enum):
    LIGHT = "Light"
    AC = "Air Conditioner"
    DEHUMIDIFIER = "Dehumidifier"

from enum import Enum


class HomeRooms(Enum):
    LIVING_ROOM = "Living Room"
    BATHROOM = "Bathroom"
    BEDROOM = "Bedroom"
    KITCHEN = "Kitchen"

from enum import Enum


class MotionSensorEvent(Enum):
    LEAVING = "Leaving"
    COMING = "Coming"

from models.Devices.AC.AC import AirConditioner
from models.Command.ACCommands import *


class ACCommandFactory:

    def __init__(self, ac: AirConditioner):
        self.ac = ac
        self.commands = []

    def create_commands(self):
        self.commands.append(ACSetCoolingCommand(self.ac))
        self.commands.append(ACSetHeatingCommand(self.ac))
        self.commands.append(ACTurnOffCommand(self.ac))

from models.Command.LightBulbCommands import *
from models.Devices.LightBulb.LightBulb import LightBulb


class LightBulbCommandFactory:

    def __init__(self, light: LightBulb) -> None:
        self.light = light
        self.commands = []

    def create_commands(self):
        self.commands.append(TurnOnLight(self.light))
        self.commands.append(TurnOffLight(self.light))
        for step in range(10, 110, 10):
            self.commands.append(SetLightBrightness(self.light, step))

from models.Command.DehumidifierCommands import TurnOffDehumidifier, TurnOnDehumidifier
from models.Devices.Dehumidifier.Dehumidifier import Dehumidifier


class DehumidifierCommandFactory:
    def __init__(self, dehumidifier: Dehumidifier):
        self.dehumidifier = dehumidifier
        self.commands = []

    def create_commands(self):
        self.commands.append(TurnOnDehumidifier(self.dehumidifier))
        self.commands.append(TurnOffDehumidifier(self.dehumidifier))

from enums.DeviceType import DeviceType
from factory.CommandFactory.ACCommandFactory import ACCommandFactory
from factory.CommandFactory.DehumidifierCommandFactory import DehumidifierCommandFactory
from factory.CommandFactory.LightBulbCommandFactory import LightBulbCommandFactory
from models.Command.DeviceCommand import DeviceCommand
from models.Home.Home import Home


class CommandFactory():
    def __init__(self, home: Home):
        self.home = home
        self.commands: list[DeviceCommand] = []

    def create_commands(self):
        for room in self.home.rooms.values():
            for device_type, device in room.devices.items():
                if device_type == DeviceType.AC:
                    ac_factory = ACCommandFactory(device)
                    ac_factory.create_commands()
                    self.commands += ac_factory.commands
                if device_type == DeviceType.LIGHT:
                    light_factory = LightBulbCommandFactory(device)
                    light_factory.create_commands()
                    self.commands += light_factory.commands
                if device_type == DeviceType.DEHUMIDIFIER:
                    dehumidifier_factory = DehumidifierCommandFactory(device)
                    dehumidifier_factory.create_commands()
                    self.commands += dehumidifier_factory.commands

from models.Devices.Dehumidifier.Dehumidifier import Dehumidifier
from models.Devices.LightBulb.LightBulb import LightBulb
from enums.DeviceType import DeviceType
from models.Devices.AC.AC import AirConditioner


class DeviceFactory:

    @staticmethod
    def create_device(device_type, name, power_consumption):
        if device_type == DeviceType.LIGHT:
            return LightBulb(name, power_consumption)
        elif device_type == DeviceType.AC:
            return AirConditioner(name, power_consumption)
        elif device_type == DeviceType.DEHUMIDIFIER:
            return Dehumidifier(name, power_consumption)

from factory.DeviceFactory.DeviceFactory import DeviceFactory
from enums.Rooms import HomeRooms
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

from abc import ABC, abstractmethod
from models.Devices.Device import Device


class Power(ABC):
    def __init__(self):
        pass

    def calculate(device: Device):
        return device.state.power_consumption()

from abc import ABC, abstractmethod
from enums.DeviceType import DeviceType

from models.Devices.DeviceState import DeviceState


class Device(ABC):

    def __init__(self, name, device_type: DeviceType, power_consumption, state: DeviceState):
        self.name = name
        self.device_type: DeviceType = device_type
        self.power_consumption = power_consumption
        self.state = state

from abc import ABC, abstractmethod


class DeviceState(ABC):

    def __init__(self):
        self.current_power = 0

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def power_consumption(self):
        pass

from abc import ABC, abstractmethod

from models.Devices.DeviceState import DeviceState


class ACState(DeviceState, ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def set_heating(self):
        pass

    @abstractmethod
    def set_cooling(self):
        pass

    @property
    def power_consumption(self):
        pass


class HeatingState(ACState):

    def __init__(self):
        super().__init__()

    def turn_off(self):

        print("Turning AC off")

    def set_heating(self):
        print("AC in heating mode")

    def set_cooling(self):
        print("AC in cooling mode")

    @property
    def power_consumption(self):
        self.current_power = 2000
        return 2000


class CoolingState(ACState):

    def __init__(self):
        super().__init__()

    def turn_off(self):
        print("Turning off AC")

    def set_heating(self):
        print("AC in heating mode")

    def set_cooling(self):
        print("AC in Cooling mode")

    @property
    def power_consumption(self):
        self.current_power = 2000
        return 2000


class OffState(ACState):

    def __init__(self):
        super().__init__()

    def turn_off(self):
        print("The device is OFF")

    def set_heating(self):
        print("AC is heating mode")

    def set_cooling(self):
        print("AC in Cooling mode")

    def power_consumption(self):
        self.current_power = 0
        return 0

from enums.DeviceType import DeviceType
from models.Devices.AC.ACState import *
from models.Devices.Device import Device


class AirConditioner(Device):

    def __init__(self, name,  power_consumption):
        super().__init__(name, DeviceType.AC, power_consumption, OffState())

    def set_heating(self):
        self.state.set_heating()
        self.state = HeatingState()
        return self.state

    def set_cooling(self):
        self.state.set_cooling()
        self.state = CoolingState()
        return self.state

    def turn_off(self):
        self.state.turn_off()
        self.state = OffState()
        return self.state

    @property
    def current_power(self):
        return self.state.power_consumption


from abc import ABC, abstractmethod
from models.Devices.DeviceState import DeviceState


class DehumidifierState(DeviceState, ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def turn_on(self):
        pass

    @property
    def power_consumption(self):
        pass


class OffState(DehumidifierState):
    def __init__(self):
        super().__init__()

    def turn_off(self):
        print("Dehumidifier is off")

    def turn_on(self):
        print("Turing on Dehumidier")

    @property
    def power_consumption(self):
        self.current_power = 0
        return 0


class OnState(DehumidifierState):
    def __init__(self):
        super().__init__()

    def turn_off(self):
        print("Turing off Dehumidier")

    def turn_on(self):
        print("Dehumidifier is on")

    @property
    def power_consumption(self):
        self.current_power = 100
        return 100

from enums.DeviceType import DeviceType
from models.Devices.Dehumidifier.DehumidifierSate import OffState, OnState
from models.Devices.Device import Device


class Dehumidifier(Device):

    def __init__(self, name, power_consumption):
        super().__init__(name, DeviceType.DEHUMIDIFIER, power_consumption, OffState())

    def turn_off(self):
        self.state.turn_off()
        self.state = OffState()
        return self.state

    def turn_on(self):
        self.state.turn_on()
        self.state = OnState()
        return self.state

    @property
    def current_power(self):
        return self.state.power_consumption

from abc import ABC, abstractmethod

from models.Devices.DeviceState import DeviceState


class LightBulbState(DeviceState, ABC):

    def __init__(self, brightness, color_temp):
        super().__init__()
        self._brightness = brightness
        self._color_temp = color_temp

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def set_color_temp(color_temp):
        pass

    @abstractmethod
    def set_brightness(brightness):
        pass

    @abstractmethod
    def update(self):
        pass

    @property
    def power_consumption(self):
        pass


class OnState(LightBulbState):

    def __init__(self):
        color_temp = 6000
        brightness = 100

        super().__init__(brightness, color_temp)

    def turn_on(self) -> LightBulbState:
        print("The light bulb is on")

    def turn_off(self) -> LightBulbState:
        print("Turning off light bulb")

    def set_color_temp(self, color_temp) -> LightBulbState:
        self._color_temp = color_temp

    def set_brightness(self, brightness) -> LightBulbState:
        self._brightness = brightness
        self._power_consumption = 0  # get power consumption

    @property
    def power_consumption(self):
        self.current_power = 5
        return self.current_power

    def update(self):
        return OffState()


class OffState(LightBulbState):

    def __init__(self):
        color_temp = 0
        brightness = 0
        power_consumption = 0
        super().__init__(brightness, color_temp)

    def turn_on(self) -> LightBulbState:
        print("Turning on light bulb")

    def turn_off(self) -> LightBulbState:
        print("The Light Bulb is off")

    def set_color_temp(self, color_temp) -> LightBulbState:
        print("The Light Bulb is off")

    def set_brightness(self, brightness) -> LightBulbState:
        print("The Light Bulb is off")

    @property
    def power_consumption(self):
        return 0

    def update(self):
        return OnState()

from enums.DeviceType import DeviceType
from models.Devices.Device import Device
from models.Devices.LightBulb.LightBulbState import *


class LightBulb(Device):
    def __init__(self, name, power_consumption):
        super().__init__(name, DeviceType.LIGHT, power_consumption, OffState())

    def turn_on(self):
        self.state.turn_on()
        self.state = OnState()
        return self.state

    def turn_off(self):
        self.state.turn_off()
        self.state = OffState()
        return self.state

    def set_brightness(self, brightness):
        self.state.set_brightness(brightness)
        return self.state

from models.Command.DeviceCommand import DeviceCommand
from models.Devices.Dehumidifier.Dehumidifier import Dehumidifier


class TurnOnDehumidifier(DeviceCommand):
    def __init__(self, dehumidifier: Dehumidifier):
        self.dehumidifier = dehumidifier

    def execute(self):
        self.dehumidifier.turn_on()


class TurnOffDehumidifier(DeviceCommand):
    def __init__(self, dehumidifier: Dehumidifier):
        self.dehumidifier = dehumidifier

    def execute(self):
        self.dehumidifier.turn_off()

from abc import ABC, abstractmethod


class DeviceCommand(ABC):

    @abstractmethod
    def execute(self):
        pass

from models.Command.DeviceCommand import DeviceCommand


class Invoker:
    def __init__(self) -> None:
        self.command_history = []

    def execute(self, command: DeviceCommand):
        command.execute()
        self.command_history.append(command)

from models.Command.DeviceCommand import DeviceCommand
from models.Devices.LightBulb.LightBulb import LightBulb


class TurnOnLight(DeviceCommand):
    def __init__(self, light_bulb: LightBulb):
        self.light_bulb = light_bulb

    def execute(self):
        self.light_bulb.turn_on()


class TurnOffLight:
    def __init__(self, light_bulb: LightBulb):
        self.light_bulb = light_bulb

    def execute(self):
        self.light_bulb.turn_off()


class SetLightBrightness:
    def __init__(self, light_bulb: LightBulb, brightness: int):
        self.light_bulb = light_bulb
        self.brightness = brightness

    def execute(self):
        self.light_bulb.set_brightness(self.brightness)

from models.Devices.AC.AC import AirConditioner
from models.Command.DeviceCommand import DeviceCommand
from models.Devices.Device import Device


class ACSetCoolingCommand(DeviceCommand):
    def __init__(self, ac: AirConditioner):
        self.ac = ac

    def execute(self):
        self.ac.set_cooling()


class ACSetHeatingCommand(DeviceCommand):
    def __init__(self, ac: AirConditioner):
        self.ac = ac

    def execute(self):
        self.ac.set_heating()


class ACTurnOffCommand(DeviceCommand):
    def __init__(self, ac: AirConditioner):
        self.ac = ac

    def execute(self):
        self.ac.turn_off()

from typing import List, Dict

from enums.Rooms import HomeRooms

from models.Home.Rooms.Rooms import Room
from simulation.human.Human import Human


class Home:
    def __init__(self, rooms: Dict[HomeRooms, Room]):
        self.rooms: Dict[HomeRooms, Room] = {room.name: room for room in rooms}
        self.house_temp = 0
        self.house_light = 0
        self.house_humidity = 0
        self.human = Human()
        # TODO: noise level

    def __getitem__(self, room):
        return self.rooms.get(room, None)

    # Setter for house_temp
    def set_house_temp(self, temp):
        self.house_temp = temp

    # Setter for house_light
    def set_house_light(self, light):
        self.house_light = light

    # Setter for house_humidity
    def set_house_humidity(self, humidity):
        self.house_humidity = humidity

    def place_human(self, room: HomeRooms):

        self.human.place_human(self.rooms[room])

from abc import ABC, abstractmethod
from ast import List
from typing import Dict

from enums.Rooms import HomeRooms


from models.Devices.Device import Device
from models.Sensors.Sensor import Sensor
from enums.DeviceType import DeviceType


class Room():

    def __init__(self, name: HomeRooms):
        self.name = name
        self.devices: Dict[DeviceType, Device] = {
        }

        self.sensors = []  # TODO: implement sensor abstract class
        self.is_human_inside = False

    def attach_device(self, device: Device):
        self.devices[device.device_type] = device

    def detach_device(self, device_type: DeviceType):
        if device_type in self.devices:
            del self.devices[device_type]

    def attach_sensor(self, sensor: Sensor):
        self.sensors.append(sensor)

    def detach_sensor(self, sensor: Sensor):
        return self.sensors.remove(sensor)

    def place_human(self):
        self.is_human_inside = True

    def remove_human(self):
        self.is_human_inside = False

from abc import ABC, abstractmethod


class Sensor(ABC):

    def __init__(self, name):
        self.name = name
        self.triggered = False

    @abstractmethod
    def trigger(self):
        pass

from main import Sensor


class HumiditySensor(Sensor):
    def __init__(self, temp_limit, name) -> None:
        super().__init__(name)

    def trigger(self):
        self.triggered = not self.triggered

from enums.MotionSensorEvents import MotionSensorEvent
from models.Sensors.Sensor import Sensor


class MotionSensor(Sensor):
    def __init__(self, name):
        super().__init__(name)

    def trigger(self):
        pass

from main import Sensor


class TemperatureSensor(Sensor):
    def __init__(self, current_temp, name) -> None:
        self.current_temp = current_temp
        super().__init__(name)

    def set_current_temp(self, current_temp):
        self.current_temp = current_temp

    def trigger(self):
        self.triggered = not self.triggered

