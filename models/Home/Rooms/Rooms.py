from abc import ABC,abstractmethod
from ast import List

from enums.Rooms import HomeRooms

from models.Devices.StateRepresentation.StateRepresentation import RepresentState

from models.Devices.Device import Device

class Room():
  
  def __init__(self , name: HomeRooms):
    self.name = name
    self.devices : List[Device] = []
    self.sensors = [] #TODO: implement sensor abstract class
    self.is_human_inside = False
    
  
  def attach_device(self,device: Device):
    self.devices.append(device)
  
  def detach_device(self,device: Device):
    return self.devices.remove(device)
  
  def print_devices_and_state(self):
    for device in self.devices:
      RepresentState.print(device)
  
  def print_sensors(self):
    for sensor in self.sensors:
      print(sensor)
  
  