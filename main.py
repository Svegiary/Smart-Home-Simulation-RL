from enums.DeviceType import DeviceType
from enums.Rooms import HomeRooms
from factory.command_factory.command_factory import CommandFactory
from factory.home_factory.home_factory import HomeFactory
from models.command.ac_commands import *
from models.command.invoker import Invoker
from representation.home_representation.print_home import PrintHome
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
commands = CommandFactory.create_commands(home)

home.place_human(HomeRooms.LIVING_ROOM)

sim = Simulation(
    timestamps,
    data,
    home,
    SimulationController(commands,
                         Invoker(),
                         home
                         ),
    config
)
print("setting runtime")

sim.set_runtime_plan(LightBulbRuntime())
print(timestamps)
print("starting runtime //////////////////////////////////////////////////////////////////////////////////")
sim.start()
print("finished runtime //////////////////////////////////////////////////////////////////////////////////")
