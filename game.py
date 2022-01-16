from utility import clear_screen, exit_game
from character.player import Player
from world.map import Map
"""Handle main gameplay loop, tracking of player information, map movement, organize and utilize game assets."""
def game_loop(start_arg=0):
    while True:
        # menu choice 'start'
        if(start_arg == 0):
            print("Starting new game...\n")
            player = player_setup() # prompt the user to setup a new character
            current_map = map_setup() # setup a map for the player
            print("You are in an area, what will you do?\n")
            print(current_map.get_map_contents()[player.get_x_coord()][player.get_y_coord()].get_info())
            current_map.get_map_contents()[player.get_x_coord()][player.get_y_coord()].show_cell_content()
            
            # test player movement
            player.change_location("right")
            print(current_map.get_map_contents()[player.get_x_coord()][player.get_y_coord()].get_info())
            current_map.get_map_contents()[player.get_x_coord()][player.get_y_coord()].show_cell_content()
            
            # test enemy creation
            player.change_location("down")
            print(current_map.get_map_contents()[player.get_x_coord()][player.get_y_coord()].get_info())
            current_map.get_map_contents()[player.get_x_coord()][player.get_y_coord()].show_cell_content()
            break
        # menu choice 'load' (to be completed)
        elif(start_arg == 1):
            print("Loading save file...\n")
            print("(NOT FUNCTIONAL)")
            print("\nExiting...")
            exit_game()
        # menu choice 'settings' (to be completed)
        elif(start_arg == 2):
            print("Settings Menu...\n")
            exit_game()

def player_setup():
    """Prompt user for a name and return a new character object with appropriate starting values."""
    name = input("Name your character: ")
    new_player = Player(name, 1, "A player character, no weapons or armor.", 0, 0)
    print(f"\nCharacter {name} created!\n")
    print("================================")
    return new_player

def map_setup():
    """Setup a map filled with cells for the player to traverse"""
    game_map = Map() # create a basic 3x3 map
    game_map.fill_map() # fill the map with content
    return game_map # return the newly created map