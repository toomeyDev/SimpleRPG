from utility import clear_screen, exit_game
"""Handle main gameplay loop, tracking of player information, map movement, organize and utilize game assets."""
def game_loop(start_arg=0):
    while True:
        # menu choice 'start'
        if(start_arg == 0):
            print("Starting new game...\n")
            print("You are in an area, what will you do?\n")
            break
        # menu choice 'load'
        elif(start_arg == 1):
            print("Loading save file...\n")
            print("(NOT FUNCTIONAL)")
            print("\nExiting...")
            exit_game()
        elif(start_arg == 2):
            print("Settings Menu...\n")
            exit_game()
            