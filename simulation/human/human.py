"""
Class for the human so that they can be placed in a room
"""

from models.home.rooms.rooms import Room


class Human:
    """
    A human class 
    """

    def __init__(self):
        self.human_location: Room = None

    def place_human(self, room: Room):
        """Place human in a room"""
        room.place_human()
        if self.human_location is not None:
            self.human_location.remove_human()
            self.human_location = room
        else:
            self.human_location = room
