from factory.HomeFactory.HomeFactory import HomeFactory
from models.Devices.LightBulb.LightBulb import LightBulb
from models.Devices.LightBulb.LightBulbSubscriber import LightBulbSubscriber
from models.Home.HomeRepresentation.PrintHome import PrintHome
from models.Sensors.MotionSensor.MotionSensor import MotionSensor
from models.Devices.StateRepresentation.StateRepresentation import RepresentState
from models.Sensors.RepresentSensor import RepresentSensor
from simulation.config.simulation_config import SimulationConfig
from simulation.data_generation.data_factories.temperature_factory import TemperatureFactory
from simulation.data_generation.timestamp_generation.timestamp import TimestampGeneration
from simulation.simulation_factory.simulation_factory import SimulationFactory


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

sim_factory = SimulationFactory(config).create_simulation()

print(sim_factory.simulation_data.temp_data)
