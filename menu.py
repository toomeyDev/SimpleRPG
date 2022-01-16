import sys
from time import sleep
from utility import clear_screen
"""Handle menu operations, start, load, exit, settings."""
class Menu:
    def __init__(self):
        self.options = ["Start", "Load", "Settings", "Exit"] # store options for the menu, start load etc
        self.menu_loop()
        
    def menu_loop(self):
        while(True):
            print("Welcome to Simple RPG Alpha 0.02")
            print("\n================================")
            while True:
                print("Start\nLoad\nSettings\nExit\n")
                print("Type your selection: ")
                ans=input().title()
                if(ans in self.options):
                    if(ans == self.options[0]):
                        print("Starting Game...")
                        break
                    elif(ans == self.options[1]):
                        print("Loading Game...")
                        break
                    elif(ans == self.options[2]):
                        print("Settings...")
                        break
                    elif(ans) == self.options[3]:
                        print("Exiting...")
                        sys.exit()
                else:
                    print("Invalid selection, please choose one of the available options.\n")
                    sleep(3)
                    clear_screen()
                    continue
            break # exit menu flow after valid selection (start, load, settings etc)