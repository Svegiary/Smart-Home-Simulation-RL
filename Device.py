from abc import ABC, abstractmethod


class Device(ABC):
  
  def __init__(self,name):
    self.name = name
  
  def turn_on(self):
    pass
  
  def turn_off(self):
    pass
    