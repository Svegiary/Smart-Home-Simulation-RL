from LightBulb.LightBulbState import OffState


class LightBulbController:
  
  def __init__(self):
    self._state = OffState()
    
  def __setState(self,state):
    self._state = state
  
  def turn_on(self):
    self.__setState(self._state.turn_on())
  def turn_off(self):
    self.__setState(self._state.turn_off())
  def set_color_temp(self, color_temp):
    self.__setState(self._state.set_color_temp())
  def set_brightness(self, brightness):
    self.__setState(self._state.set_brightness())
    
  @property
  def state(self):
    return self._state
  