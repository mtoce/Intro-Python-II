from room import Room
from player import Player
from item import Item
from termcolor import colored

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

# Room links
locations['outside'].n_to = locations['foyer']
locations['foyer'].s_to = locations['outside']
locations['foyer'].n_to = locations['overlook']
locations['foyer'].e_to = locations['narrow']
locations['overlook'].s_to = locations['foyer']
locations['narrow'].w_to = locations['foyer']
locations['narrow'].n_to = locations['treasure']
locations['treasure'].s_to = locations['narrow']

# Add items to rooms
locations['treasure'].items.append(Item('goblet', 'A shiny cup that can be used to hold your liquor'))
locations['outside'].items.append(Item('tulip', 'A beautiful periwinkle-colored flower'))
locations['outside'].items.append(Item('rose', 'A beautiful flower that women adore'))
def move(direction):
    '''
    Move function for the player.
    '''

    if hasattr(player.room, direction+"_to"):
        player.room = getattr(player.room, direction+"_to")
    else:
        print(colored(
            "\nUnfortunately, there isn't a room there. Try another direction.", 'red'))


def game_help():
    print('''
    Controls:

    Moving instructions:
    Move North: n, N, north, North, Up, up
    Move South: s, S, south, South, Down, down
    Move East: e, E, east, East, Right, right
    Move West: w, W, west, West, Left, left

    General instructions:
    Show this help screen: ?, help, Help
    Quit the game: q, Q, quit, Quit, Q, exit, Exit, bye, leave
    ''')

def item_transfer(item, grabbing):
    '''
    Item pickup/drop function
    '''
    item = item.lower()
    # if grabbing the item (grabbing is a boolean variable: same as (if grabbing == True)
    if grabbing:
        # if item name is found in the room
        if item in [c.name for c in player.room.items]:
            # use this dual syntax since we need to use c in player.room.items.pop(c)
            for c, item_object in enumerate(player.room.items):
                if item_object.name == item:
                    player.items.append(player.room.items.pop(c))
                    print("You grabbed the ", item)
        # if item name isn't in room
        else:
            print("Seems as though that item isn't here...")
    # if dropping an item
    else:
        # checks that the item is in the players current "inventory"
        if item in [c.name for c in player.items]:
            # iterate thru player's item list and get item pbject via index
            # use this dual syntax since we need to use c in player.items.pop(c)
            for c, item_object in enumerate(player.items):
                if item_object.name == item:
                    player.room.items.append(player.items.pop(c))
                    print("You dropped the ", item)
        else:
            print("You aren't carrying that item with you!")

def search_room():
    '''
    Searches the player's current room for items
    '''
    print("Current items inside this room: ", colored([f"{item.name}: {item.desc}" for item in player.room.items], 'magenta'))


def inspect():
    '''
    Inspects the items in a players inventory
    '''

def inventory():
    '''
    Current inventory list for the player
    '''
    if len(player.items) >= 1:
        print("Your current inventory: ")
        for item in player.items:
            print(item.name, "\n")
    else:
        print("You currently aren't holding any items! Try using command ", colored('grab + item name', 'magenta'))

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
    # allowable search actions by user
    search_list = ['search', 'Search', 'look', 'Look', 'find', 'Find']
    # allowable item acquisition actions by user
    item_pickup_list = ['grab', 'take', 'Grab', 'Take',
                        'get', 'Get', 'yoink', 'Yoink', 'gather', 'Gather']
    # allowable item drop actions by user
    item_drop_list = ['drop', 'Drop', 'put', 'Put', 'throw', 'Throw']
    # allowable inventory actions by user
    inventory_list = ['i', 'inv', 'inventory',
                      'I', 'Inv', 'Inventory', 'items', 'Items']
    # allowable search actions by user
    search_list = ['search', 'Search', 'look', 'Look', 'inspect', 'Inspect']
    # allowable help actions by user
    help_list = ['help', '?', 'Help']

    # Simplify user imput
    # splits user unput by spaces
    user_input_list = user_input.split()
    # if user inputs nothing, will append a space so the program doesn't break
    if not user_input_list:
        user_input_list.append('')
    # Take only the first word the user types as a command
    user_input = user_input_list[0]

    # print(user_input_list)
    if user_input in north_list:
        move('n')
    elif user_input in south_list:
        move('s')
    elif user_input in east_list:
        move('e')
    elif user_input in west_list:
        move('w')
    elif user_input in exit_list:
        global wants_to_quit
        wants_to_quit = True
    elif user_input in help_list:
        game_help()
    elif user_input in search_list:
        search_room()
    elif user_input in item_pickup_list:
        # check to see that the item is specified
        if len(user_input_list) > 1:
            item_transfer(user_input_list[1], grabbing=True)
        else:
            print("You can't decide what to grab")
    elif user_input in item_drop_list:
        if len(user_input_list) > 1:
            item_transfer(user_input_list[1], grabbing=False)
        else:
            print("You go to drop something, but decided it looked pretty cool and kept it instead.")
    elif user_input in inventory_list:
        inventory()
    else:
        print("\nSorry, but that is an invalid command. Type '?' or 'help' for allowable commands")


if __name__ == "__main__":

    wants_to_quit = False
    # initialize the game (player name, starting room=outside, and room description)
    print("\n")
    player = Player(input("Choose a username: "), locations["outside"])

    # create game loop
    moves = 0
    while not wants_to_quit:
        print("\nNumber of times player has moved: ",
              colored(f"{moves}", 'yellow'))
        print("Current Room: ", colored(f"{player.room.name}", 'cyan'))
        print("Room Description: ", colored(f"{player.room.desc}\n", 'cyan'))
        print("Player Inventory: ", colored([f"{item.name}: {item.desc}" for item in player.items if len(player.items) >= 1], 'magenta'))

        command = input(colored("User Action: ", 'green'))
        action(command.lower())
        moves += 1
