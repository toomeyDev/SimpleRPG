from array import *
from world.cell import Cell
"""Module representing a map made up of cells for entities to traverse."""
class Map:
    def __init__(self, x=3, y=3):
        self.dim_x = x
        self.dim_y = y

        # setup map grid (x * y size) based on provided initial values
        self.map_cells = [[Cell() for r in range(self.dim_x)] for c in range(self.dim_y)]
        
    def show_map_contents(self):
        for r in self.map_cells:
            for c in r:
                print(c.get_info())
                c.show_cell_content()