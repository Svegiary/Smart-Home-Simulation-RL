from LightBulbState import OffState,OnState
from Device import Device

def LightBulb(Device):
  def __init__(self,name, power_consumption):
    self._state = OffState()
    
    
  @property
  def state(self):
    return self._state