from menu import Menu
import game
print("Simple RPG 0.02\n")
while(True):
    game_menu = Menu()
    game.game_loop(game_menu.get_selection())
    break