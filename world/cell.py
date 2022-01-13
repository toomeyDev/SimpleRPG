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