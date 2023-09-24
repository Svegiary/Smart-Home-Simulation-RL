from simulation.HomeTempCalculator import HomeTempCalculator


class SimulationSnapshot:
    def __init__(self, inside_temp, outside_temp, temp: HomeTempCalculator):
        self.outside_temp = outside_temp
        print("Outside", outside_temp)
        print("Inside", temp.home.house_temp)
        self.inside_temp = temp.calculate_temp(outside_temp)

        self.commands = []
        self.human_location = 0

    def print(self):
        print("Outside temp")
        print(self.outside_temp)
        print("Inside temp")
        print(self.inside_temp)


class SnapshotEvaluation:
    pass
