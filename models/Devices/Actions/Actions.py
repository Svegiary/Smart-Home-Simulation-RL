from abc import ABC, abstractmethod
from typing import Callable


class Action(ABC):
    def __init__(self, action: Callable):
        self.action: Callable = action

    @abstractmethod
    def perform_action(self):
        pass
