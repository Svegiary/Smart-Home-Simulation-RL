from ast import List

from models.Devices.StateRepresentation.StateRepresentation import RepresentState
from models.Devices.Device import Device


class PrintDevices:
  
  @staticmethod 
  def present(self, devices : List[Device]):
    for device in devices:
      RepresentState.print(device)