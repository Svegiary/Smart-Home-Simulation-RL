from abc import ABC, abstractmethod

class LightBulbState(ABC):
  @abstractmethod
  def turn_on(self):
    pass 
  
  @abstractmethod
  def turn_off(self):
    pass
  
  @abstractmethod
  def set_color_temp(color_temp):
    pass
  
  @abstractmethod
  def calculate_power_consumption(self):
    pass
  
class OnState(LightBulbState):
  def turn_on(self):
    print("The light bulb is on")
  def turn_off(self):
    print("Turning off light bulb")
    return 

class OffState(LightBulbState):
  def turn_on(self):
    return OnState()
  def turn_off(self):
    print("The Light Bulb is off")
    