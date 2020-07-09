from room import Room
from player import Player
# Declare all the rooms

locations = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

locations['outside'].n_to = locations['foyer']
locations['foyer'].s_to = locations['outside']
locations['foyer'].n_to = locations['overlook']
locations['foyer'].e_to = locations['narrow']
locations['overlook'].s_to = locations['foyer']
locations['narrow'].w_to = locations['foyer']
locations['narrow'].n_to = locations['treasure']
locations['treasure'].s_to = locations['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# player = Player(input("What's your name?"), "outside", locations["outside"])
# print(my_player)
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def move(direction):
    '''
    Move function for the player.
    '''
    # Where is the player currently located?
    loc = player.room
    
    direction = input("In which cardinal direction would you like to move?")
    
    if hasattr(loc, direction + "_to"):
        loc = getattr(loc, direction + "_to")
    else:
        print("Unfortunately, there isn't a room there, try another direction.")

def action(user_input):
    '''
    Handles multiple actions the player can take, i.e. move, item pick-up, and item-drop
    '''

    # allowable directions by user
    north_list = ['n', 'N', 'north', 'North', 'Up', 'up']
    south_list = ['s', 'S', 'south', 'South', 'Down', 'down']
    east_list = ['e', 'E', 'east', 'East', 'Right', 'right']
    west_list = ['w', 'W', 'west', 'West', 'Left', 'left']

    # allowable quit actions by user
    exit_list = ['exit', 'Exit', 'quit', 'Quit', 'q', 'Q', 'bye', 'leave']

    # allowable item acquisition actions by user
    item_pickup_list = ['grab', 'take', 'Grab', 'Take', 'get', 'Get', 'yoink', 'Yoink', 'gather', 'Gather']

    # allowable item drop actions by user
    item_drop_list = ['drop', 'Drop', 'put', 'Put', 'throw', 'Throw']

    # allowable inventory actions by user
    inventory_list = ['i', 'inv', 'inventory', 'I', 'Inv', 'Inventory', 'items', 'Items']

    # allowable search actions by user
    search_list = ['search', 'Search', 'look', 'Look', 'inspect', 'Inspect']

    # allowable help actions by user
    help_list = ['help', '?', 'Help']

    user_input_list = user_input.split()

    # if user inputs nothing, will append a space so the program doesn't break
    if not user_input_list:
        user_input_list.append('')

    # Take the first action the user wants to do
    user_input = user_input_list[0]
    print(user_input_list)
    if user_input in north_list:
        move('n')
    elif user_input in south_list:
        move('s')
    elif user_input in east_list:
        move('e')
    elif user_input in west_list:
        move('w')
    elif user_input in help_list:
        global wants_to_quit
        wants_to_quit = True

if __name__ == "__main__":
    wants_to_quit = False
    # initialize the game (player name, starting room=outside, and room description)
    print("\n")
    player = Player(input("What's your name?  "), "outside", locations["outside"])

    # create loop for player to move between rooms
    for moves in range(1000):
        print("\n")
        print(f"Number of times player has moved: {moves} \n")
        print(f"Player Name: {player.name}")
        print(f"Current Room: {player.room}")
        print(f"Room Description: {locations.get(player.room)} \n")
        #print("\n")
        #direction = input("In which cardinal direction would you like to move?  ")
        action(input("What action would you like to take? "))
