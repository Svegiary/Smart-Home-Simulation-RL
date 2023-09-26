from models.Home.Rooms.Rooms import Room


class Human:
    def __init__(self):
        self.human_location: Room = None

    def place_human(self, room: Room):
        room.place_human()
        if self.human_location is not None:
            self.human_location.remove_human()
            self.human_location = room
        else:
            self.human_location = room
