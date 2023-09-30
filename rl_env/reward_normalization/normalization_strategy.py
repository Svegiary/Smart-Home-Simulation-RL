from abc import ABC, abstractmethod
import math
import numpy as np
from simulation.config.simulation_config import SimulationConfig

from simulation.preferences.simulation_preferences import Preferences
"""
Normalization techinques from here
https://en.wikipedia.org/wiki/Feature_scaling
"""


class NormalizationStrategy(ABC):

    @abstractmethod
    def normalize(self, reward: float, max_reward: float, min_reward: float) -> float:
        pass


class ZScoreNormalization(NormalizationStrategy):

    def __init__(self, rewards: list[float]) -> None:
        self.mean = sum(rewards) / len(rewards)
        self.standard_deviation = math.sqrt(
            sum((x - self.mean) ** 2 for x in rewards) / len(rewards))

    def normalize(self, reward: float):
        return (reward - self.mean) / self.standard_deviation


class MinMaxNormalization(NormalizationStrategy):
    def __init__(self,) -> None:
        pass

    def normalize(self, reward: float, max_reward, min_reward):
        return (reward - min_reward) / (max_reward - min_reward)
