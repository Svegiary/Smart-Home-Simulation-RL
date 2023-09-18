from abc import ABC,abstractmethod
from ast import List

from models.Devices.StateRepresentation.StateRepresentation import RepresentState

from models.Devices.Device import Device

class Room(ABC):
  
  def __init__(self):
    self.devices : List[Device] = []
    self.sensors = [] #TODO: implement sensor abstract class
    self.is_human_inside = False
    
  
  @abstractmethod
  def attach_device(self,device: Device):
    pass
  
  @abstractmethod
  def detach_device(self,device: Device):
    pass
  
  def print_devices_and_state(self):
    for device in self.devices:
      RepresentState.print(device)
  
  def print_sensors(self):
    for sensor in self.sensors:
      print(sensor)
  