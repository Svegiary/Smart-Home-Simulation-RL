from models.Devices.AC.ACState import *
from models.Devices.DeviceController import DeviceController


class AcController(DeviceController):
    def __init__(self):
        super().__init__(OffState())

    def _setState(self, state):
        self._state = state

    def set_heating(self):
        self._state.set_heating()
        self._setState(HeatingState())
        return self.state

    def set_cooling(self):
        self._state.set_cooling()
        self._setState(CoolingState())
        return self.state

    @property
    def state(self):
        return self._state
