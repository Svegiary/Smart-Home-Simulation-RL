class SimulationSnapshot:
    def __init__(self, inside_temp, outside_temp):
        self.inside_temp = inside_temp
        self.outside_temp = outside_temp
        self.commands = []
        self.human_location = 0


class SnapshotEvaluation:
    pass
