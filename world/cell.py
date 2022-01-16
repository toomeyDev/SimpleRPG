from character.enemy import Enemy
"""Module representing a single cell within a larger map entity."""
class Cell:
    def __init__(self, x=0, y=0, description="An empty cell with nothing interesting present.."):
        self.x = x
        self.y = y
        self.description = description

        # contains events, enemies, NPCs, items present in this cell
        self.cell_content = []
    
    def get_info(self):
        output = "Cell coordinates: \nx: "
        output += (str(self.x) + " y: " + str(self.y))
        output += "\n"
        output += self.description
        return output

    def set_coordinates(self, x=0,y=0):
        """Set the coordinates of this cell."""
        self.x = x
        self.y = y
        
    def add_cell_content(self, content):
        """Add content to this cell."""
        self.cell_content.append(content)

    def remove_cell_content(self, item):
        """Remove specified content from this cell."""
        self.cell_content.remove(item)

    def show_cell_content(self):
        """Print the contents of this cell."""
        for item in self.cell_content:
            print(item)

    def set_cell_description(self, description):
        """Set the description of this cell."""
        self.description = description

    def add_test_enemy(self):
        """Add an enemy with default values to this cell for testing."""
        self.cell_content.append(Enemy())

    def add_enemy(self, name="Default", lvl=1, description="Default", hp=10, atk=1, exp=1, ASCII=":)"):
        """Add an enemy with the specified values to this cell."""
        self.cell_content.append(Enemy(name, lvl, description, atk, exp, ASCII))