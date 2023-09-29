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
        # self.target_noise = None

    def set_preferences(self, preferences: Dict):
        self.target_temp = preferences["target_temp"]
        self.target_hum = preferences["target_humidity"]
        self.target_luminance = preferences["target_luminance"]
        # self.target_noise = preferences["target_noise"]
