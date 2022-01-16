import sys
from time import sleep
from utility import clear_screen, exit_game
"""Handle menu operations, start, load, exit, settings."""
class Menu:
    def __init__(self):
        self.options = ["Start", "Load", "Settings", "Exit"] # store options for the menu, start load etc
        self.menu_selection = -1
        self.menu_loop() # execute main menu loop, should set menu selection to valid option (0 thru 2)
        
    def menu_loop(self):
        while(True):
            print("Welcome to Simple RPG Alpha 0.03")
            print("\n================================")
            while True:
                print("Start\nLoad\nSettings\nExit\n")
                print("Type your selection: ")
                ans=input().title()
                if(ans in self.options):
                    if(ans == self.options[0]):
                        print("================================")
                        self.menu_selection = 0
                        break
                    elif(ans == self.options[1]):
                        print("================================")
                        self.menu_selection = 1
                        break
                    elif(ans == self.options[2]):
                        print("================================")
                        self.menu_selection = 2
                        break
                    elif(ans) == self.options[3]:
                        print("================================")
                        exit_game()
                else:
                    print("Invalid selection, please choose one of the available options.\n")
                    sleep(2)
                    clear_screen()
                    continue
            break # exit menu flow after valid selection (start, load, settings etc)

    def get_selection(self):
        """Return the currently selected menu option."""
        return self.menu_selection