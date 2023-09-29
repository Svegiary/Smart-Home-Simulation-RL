import gym


import gym
from gym import spaces
from enums.Rooms import HomeRooms
from factory.command_factory.command_factory import CommandFactory
from factory.home_factory.home_factory import HomeFactory
from models.command.device_command import DeviceCommand
from models.command.invoker import Invoker
from rl_env.math_functions import MathFunctions
from simulation.Simulation import Simulation
from simulation.SimulationRuntime import LightBulbRuntime

from simulation.config.simulation_config import SimulationConfig
from simulation.data_generation.data_factories.humidity_factory import HumidityFactory
from simulation.data_generation.data_factories.sunlight_factory import SunlightFactory
from simulation.data_generation.data_factories.temperature_factory import TemperatureFactory
from simulation.data_generation.simulation_data_factory import SimulationDataFactory
from simulation.data_generation.timestamp_generation.timestamp import TimestampGeneration
from simulation.preferences.simulation_preferences import Preferences


class SimulationEnv(gym.Env):
    """Custom Environment that follows gym interface"""

    def __init__(self):
        super(SimulationEnv, self).__init__()
        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions:
        self.action_space = spaces.Discrete(N_DISCRETE_ACTIONS)
        # Example for using image as input (channel-first; channel-last also works):
        self.observation_space = spaces.Box(low=0, high=255,
                                            shape=(N_CHANNELS, HEIGHT, WIDTH), dtype=np.uint8)

    def temp_evaluation(self, current_temp: float):
        return MathFunctions.temp_reward(current_temp,
                                         self.preferences.target_temp,
                                         self.config,
                                         )

    def step(self, action: DeviceCommand):
        try:
            timestamp = next(self.timestamp_iterator)
        except StopIteration:
            self.done = True
            return self.observation, self.reward, self.done, self.info

        self.invoker.execute(action)
        self.snapshot = self.sim.extract_snapshot(timestamp)

        self.observation = [
            self.home.house_temp,
            self.home.house_humidity,
            self.home.house_light,
            self.preferences.target_temp,
            self.preferences.target_hum,
            self.preferences.target_luminance,
            self.invoker.command_history,
            self.snapshot.current_power
        ]

        return self.observation, reward, done, info

    def reset(self):

        self.done = False

        self.config = SimulationConfig()
        constraints = {
            "max_temp": 30,
            "min_temp": 10,
            "max_humidity": 100,
            "min_humidity": 0,
            "min_luminance": 0.0,
            "max_luminance": 1.0
        }
        print(constraints)

        self.config.set_constraints(constraints)

        simulation_params = {
            "time_interval": 10,  # minutes
            "simulation_duration": 24
        }

        self.config.set_simulation_params(simulation_params)

        self.preferences = Preferences()

        pref = {
            "target_temp": 24,
            "target_humidity": 60,
            "target_luminance": 0.8

        }

        self.preferences.set_preferences(pref)

        self.timestamps = TimestampGeneration(self.config)
        self.timestamps.generate_timestamps()

        self.temp_factory = TemperatureFactory(self.config, self.timestamps)
        self.humidity_factory = HumidityFactory(self.config, self.timestamps)
        self.sunlight_factory = SunlightFactory(self.config, self.timestamps)

        self.data = SimulationDataFactory.create_simulation_data(
            self.temp_factory, self.humidity_factory, self.sunlight_factory)

        self.home = HomeFactory.create_home()

        self.commands = CommandFactory.create_commands(self.home)

        self.home.place_human(HomeRooms.LIVING_ROOM)

        self.sim = Simulation(
            self.timestamps,
            self.data,
            self.home,
            self.config

        )
        self.sim.set_runtime_plan(LightBulbRuntime())
        self.invoker = Invoker()

        self.timestamp_iterator = self.timestamps.timestamp_iterator()

        # [ internal_data , user_preferences , action_history , power_consumption]
        first = self.timestamps.timestamps[0]
        self.home.set_house_humidity = self.sim.simulation_data.humidity_data[first]
        self.home.set_house_light = self.sim.simulation_data.sunlight_data[first]
        self.home.set_house_temp = self.sim.simulation_data.temp_data[first]
        self.snapshot = self.sim.extract_snapshot(first)

        self.observation = [
            self.home.house_temp,
            self.home.house_humidity,
            self.home.house_light,
            self.preferences.target_temp,
            self.preferences.target_hum,
            self.preferences.target_luminance,
            self.invoker.command_history,
            self.snapshot.current_power
        ]

        return self.observation

    def render(self, mode='human'):
        pass

    def close(self):
        pass
