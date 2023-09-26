from simulation.SnapshotDataCalculator import SnapshotDataCalculator


class SimulationSnapshot:
    def __init__(self, outside_temp, outside_humidity, calculator: SnapshotDataCalculator):
        self.outside_temp = outside_temp
        self.outside_humidity = outside_humidity
        self.inside_temp = calculator.calculate_temp(outside_temp)
        self.inside_humidity = calculator.calculate_humidity(outside_humidity)

        self.human_location = 0

    def print(self):
        print("//////////////////////////////////////////////")
        print("Outside temp : ", self.outside_temp,
              "| Inside temp : ", self.inside_temp)
        print("---------------------------")
        print("Outside humidity : ", self.outside_humidity,
              "| Inside humidity : ", self.inside_humidity)
        print


class SnapshotEvaluation:
    pass
