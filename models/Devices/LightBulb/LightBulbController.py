from models.Devices.DeviceController import DeviceController
from models.Devices.LightBulb.LightBulbState import OffState, OnState
from models.Devices.StateObservation.Observer import Observer


class LightBulbController(DeviceController, Observer):

    def __init__(self):
        super().__init__(OffState())

    def _setState(self, state):
        self._state = state

    def turn_on(self):
        self._state.turn_on()
        self._setState(OnState())
        return self.state

    def turn_off(self):
        self._state.turn_off()
        self._setState(OffState())
        return self.state

    def set_color_temp(self, color_temp):
        self._state.set_color_temp(color_temp)
        return self.state

    def set_brightness(self, brightness):
        self._state.set_brightness(brightness)
        return self.state

    def update(self):
        if self.state is OnState():
            self._setState(OffState())
            return self.state
        else:
            self._setState(OnState())
            return self.state

    @property
    def state(self):
        return self._state
