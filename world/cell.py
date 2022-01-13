"""Module representing a single cell within a larger map entity."""
class Cell:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def get_info(self):
        output = "Cell coordinates: \nx: "
        output += (str(self.x) + " y: " + str(self.y))
        return output