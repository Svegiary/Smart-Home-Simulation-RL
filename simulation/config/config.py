class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance.initialize_config()
        return cls._instance

    def initialize_config(self, time_interval, simulation_duration):
        self.time_interval = time_interval
        self.simulation_duration = simulation_duration
