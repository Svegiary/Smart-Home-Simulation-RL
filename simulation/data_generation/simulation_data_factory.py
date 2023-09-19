from simulation.data_generation.data_factories.temperature_factory import TemperatureFactory
from simulation.data_generation.simulation_data import SimulationData


class SimulationDataFactory:
    @staticmethod
    def create_simulation_data(temp_factory: TemperatureFactory, humidity_factory, sunlight_factory):  # add types
        temp_factory.generateTempData()
        t = temp_factory.data

        return SimulationData(t, 0, 0)
