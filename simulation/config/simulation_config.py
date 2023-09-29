"""
Config singleton class for setting up simulation parameters and constraints.


"""


from typing import Dict


class SimulationConfig:
    """
    Config singleton class for setting up simulation parameters and constraints.
    simulation_duration: hours , >1
    time_interval: minutes, >1
    """
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
        self.min_luminance: float = None
        self.max_luminance: float = None

    def set_constraints(self, constraints: Dict[str, float]):
        """
        Setting the environment constraints for the simulation.
        """
        self.max_temp = constraints["max_temp"]
        self.min_temp = constraints["min_temp"]
        self.max_humidity = constraints["max_humidity"]
        self.min_humidity = constraints["min_humidity"]
        self.min_luminance = constraints["min_luminance"]
        self.max_luminance = constraints["max_luminance"]

    def set_simulation_params(self, simulation_params: Dict[str, int]):
        """
        Time interval for refreshing the simulation and the simulation duration
        """
        self.time_interval = simulation_params["time_interval"]
        self.simulation_duration = simulation_params["simulation_duration"]
