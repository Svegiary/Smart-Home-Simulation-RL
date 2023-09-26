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
