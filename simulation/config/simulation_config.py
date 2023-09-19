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
