"""
Class for encapsulating simulation data. If we have many types of data
this become increasingly more useful.
"""


from typing import Dict


class SimulationData:
    """
    Encapsulates simulation data
    """

    def __init__(self, temp_data: Dict[int, float], humidity_data: Dict[int, float], sunlight_data: Dict[int, float]):
        self.temp_data = temp_data
        self.humidity_data = humidity_data
        self.sunlight_data = sunlight_data

    def get_data_for_timestamp(self, timestamp: int) -> Dict[str, float]:
        """
        Get a dict of the data for a given timestamp
        """
        return {
            "temp": self.temp_data[timestamp],
            "sunlight": self.sunlight_data[timestamp],
            "humidity": self.humidity_data[timestamp]
        }
