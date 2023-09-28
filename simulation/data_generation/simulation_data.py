"""
Class for encapsulating simulation data. If we have many types of data
this become increasingly more useful.
"""


from typing import Dict


class SimulationData:
    # TODO: add types
    def __init__(self, temp_data: Dict[int, float], humidity_data: Dict[int, float], sunlight_data: Dict[int, float]):
        self.temp_data = temp_data
        self.humidity_data = humidity_data
        self.sunlight_data = sunlight_data
