from array import *
from world.cell import Cell
"""Module representing a map made up of cells for entities to traverse."""
class Map:
    def __init__(self, x=3, y=3):
        self.dim_x = x
        self.dim_y = y

        self.map_cells = [[Cell() for r in range(self.dim_x)] for c in range(self.dim_y)]
        print(self.map_cells[0][1].get_info())
