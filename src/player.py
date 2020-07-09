# Write a class to hold player information, e.g. what room they are in
# currently.

# from room import Room

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        #self.player_items = player_items

    def __str__(self):
        return f"Hello {self.name}, you are in the {self.room}"