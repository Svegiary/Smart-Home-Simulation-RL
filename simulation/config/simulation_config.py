"""
Config singleton class for setting up simulation parameters and constraints.

Attributes:
    time_interval (int or None): Time interval for simulation updates.
    simulation_duration (int or None): Total duration of the simulation.
    max_temp (float or None): Maximum allowed temperature constraint.
    min_temp (float or None): Minimum allowed temperature constraint.
    max_humidity (float or None): Maximum allowed humidity constraint.
    min_humidity (float or None): Minimum allowed humidity constraint.

"""


from typing import Dict


class SimulationConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SimulationConfig, cls).__new__(cls)
            cls._instance.initialize_config()
        return cls._instance

    def initialize_config(self):
        self.time_interval: int = None
        self.simulation_duration: int = None
        self.max_temp: float = None
        self.min_temp: float = None
        self.max_humidity: float = None
        self.min_humidity: float = None

    def set_constraints(self, constraints: Dict[str, float]):
        self.max_temp = constraints["max_temp"]
        self.min_temp = constraints["min_temp"]
        self.max_humidity = constraints["max_humidity"]
        self.min_humidity = constraints["min_humidity"]

    def set_simulation_params(self, simulation_params: Dict[str, int]):
        self.time_interval = simulation_params["time_interval"]
        self.simulation_duration = simulation_params["simulation_duration"]
