from character.character import Character
from character.player import Player
from world.cell import Cell
from world.map import Map
print("Simple RPG 0.01\n")

test = Character()
print(test.get_info())

test_cell = Cell()
print(test_cell.get_info())

test_map = Map()
test_player = Player()
print(test_player.get_info())