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
    "time_interval": 10,
    "simulation_duration": 24
}
config.set_simulation_params(simulation_params)

timestamps = TimestampGeneration(config)
timestamps.generate_timestamps()
temp_factory = TemperatureFactory(config, timestamps)
humidity_factory = HumidityFactory(config, timestamps)
sunlight_factory = 0  # TODO:implement

data = SimulationDataFactory.create_simulation_data(
    temp_factory, humidity_factory, sunlight_factory)

home = HomeFactory().create_home()

PrintHome.print(home)
command_Factory = CommandFactory(home)
command_Factory.create_commands()

sim = Simulation(
    timestamps,
    data,
    home,
    SimulationController(command_Factory.commands,
                         Invoker()
                         ))
print("setting runtime")

sim.set_runtime_plan(ControllerDehumidifierRuntime())
print(timestamps)
print("starting runtime //////////////////////////////////////////////////////////////////////////////////")
sim.start()
print("finished runtime //////////////////////////////////////////////////////////////////////////////////")
