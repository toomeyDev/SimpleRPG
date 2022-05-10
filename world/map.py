from array import *
from world.cell import Cell
"""Module representing a map made up of cells for entities to traverse."""
class Map:
    def __init__(self, x=3, y=3):
        self.dim_x = x
        self.dim_y = y

        # setup map grid (x * y size) based on provided initial values
        self.map_cells = [[Cell() for r in range(self.dim_x)] for c in range(self.dim_y)]

    def get_map_contents(self):
        """Return the map content grid of this map object."""
        return self.map_cells

    def get_cell_at(self, x=0, y=0):
        """Access the cell at specified coordinates."""
        return self.get_map_contents()[x][y]

    def show_map_contents(self):
        for r in self.map_cells:
            for c in r:
                print("*")

    def set_map_cell(self, x, y, description, content):
        """Set the description and append content to the selected map cell."""
        self.map_cells[x][y].set_coordinates(x,y)
        self.map_cells[x][y].set_cell_description(description)
        self.map_cells[x][y].add_cell_content(content)

    def fill_map(self):
        """Fill a map with content for the player character to encounter."""
        for r in range(self.dim_x):
            for c in range(self.dim_y):
                self.set_map_cell(r, c,"A wooded clearing, with a few rocks scattered about.", "Rocks")
        self.set_map_cell(1, 0, "A dark scary cave..", "Spiders, rocks, barrels, treasure")
        self.get_cell_at(1, 0).add_test_enemy() # add an enemy to a cell for testing purposes
        self.set_map_cell(1, 1, "A tall mountain blocks the way.", "Trees, rocks, boxes.")
        self.get_cell_at(1,1).add_enemy("Slime", 2, "A slimy slime sits in the way.", 25, 5, 15, "{0-0}")