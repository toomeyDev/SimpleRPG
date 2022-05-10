from menu import Menu
import game
from lib import fileIO
print("Simple RPG 0.03\n")
while(True):
    fileIO.load_map('world\maps\\testmap.txt')
    game_menu = Menu() # run main-menu sequence
    game.game_loop(game_menu.get_selection()) # main gameplay sequence
    # write changes to .txt file for saving
    break