from character.character import Character
from character.player import Player
from world.cell import Cell
from world.map import Map
print("Simple RPG 0.01\n")

test = Character()
print(test.get_info())

test_cell = Cell()
print(test_cell.get_info())
test_cell.set_cell_description("A testing cell for testing out new features..")
print(test_cell.get_info())
test_cell.add_cell_content("An item")
test_cell.show_cell_content()

test_map = Map()
test_map.show_map_contents()
test_player = Player()
print(test_player.get_info())