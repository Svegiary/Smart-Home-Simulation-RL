from abc import ABC, abstractmethod

from models.DeviceState import DeviceState


class LightBulbState(DeviceState, ABC):

    def __init__(self, power_consumption, brightness, color_temp):
        super().__init__(power_consumption)
        self._brightness = brightness
        self._color_temp = color_temp

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
    def set_brightness(brightness):
        pass

    @property
    def power_consumption(self):
        return self._power_consumption


class OnState(LightBulbState):

    def __init__(self):
        color_temp = 6000
        brightness = 100
        power_consumption = 10
        super().__init__(power_consumption, brightness, color_temp)

    def turn_on(self) -> LightBulbState:
        print("The light bulb is on")
        return self

    def turn_off(self) -> LightBulbState:
        print("Turning off light bulb")
        return OffState()

    def set_color_temp(self, color_temp) -> LightBulbState:
        self._color_temp = color_temp
        return self

    def set_brightness(self, brightness) -> LightBulbState:
        self._brightness = brightness
        self._power_consumption = 0  # get power consumption
        return self


class OffState(LightBulbState):

    def __init__(self):
        color_temp = 0
        brightness = 0
        power_consumption = 0
        super().__init__(power_consumption, brightness, color_temp)

    def turn_on(self) -> LightBulbState:
        return OnState()

    def turn_off(self) -> LightBulbState:
        print("The Light Bulb is off")
        return self

    def set_color_temp(self, color_temp) -> LightBulbState:
        print("The Light Bulb is off")
        return self

    def set_brightness(self, brightness) -> LightBulbState:
        print("The Light Bulb is off")
        return self
