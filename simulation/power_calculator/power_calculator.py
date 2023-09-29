from simulation.SimulationSnapshot import SimulationSnapshot
from simulation.config.simulation_config import SimulationConfig
from simulation.home_devices_snapshot.home_device_snapshot import HomeDeviceSnapshot


class PowerCalculator:
    """
    Class to calculate the power consumption during the simulation
    """

    @staticmethod
    def kwh(power: int) -> float:
        """
        Calculate kwh
        """
        config = SimulationConfig()
        power_kilowatts = power / 1000
        time_hours = config.time_interval / 60
        return power_kilowatts * time_hours

    @staticmethod
    def calculate_power(device_snapshot: HomeDeviceSnapshot) -> float:
        """
        Total energy in a Simulation snapshot in kwh
        """
        device_snapshot.count_all()
        total_power = 0.0
        for device in device_snapshot.active_devices:
            device_power = device.current_power()
            energy = PowerCalculator.kwh(device_power)
            total_power += energy
        return total_power

    @staticmethod
    def calculate_total_energy(snapshots: list[SimulationSnapshot]) -> float:
        """
        Total Energy consumed during the simulation in kwh
        """
        total_power = sum(snapshot.current_power for snapshot in snapshots)
        return total_power
