from models.Controller import DeviceController
from models.LightBulb.LightBulbState import OffState


class LightBulbController(DeviceController):

    def __init__(self):
        super().__init__(OffState())

    def _setState(self, state):
        self._state = state

    def turn_on(self):
        self._setState(self._state.turn_on())

    def turn_off(self):
        self._setState(self._state.turn_off())

    def set_color_temp(self, color_temp):
        self._setState(self._state.set_color_temp(color_temp))

    def set_brightness(self, brightness):
        self._setState(self._state.set_brightness(brightness))

    @property
    def state(self):
        return self._state
