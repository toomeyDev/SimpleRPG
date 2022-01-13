from character.character import Character
class Player(Character):
    def __init__(self, name="default", lvl=0, description="default player", location_x=0, location_y=0):
        super().__init__(name, lvl, description)
        
        # player location (x,y coordinates)
        self.location_x = location_x
        self.location_y = location_y
        
        # player attributes (HP, atk, exp)
        self.health = 100
        self.attack = 1
        self.exp = 0

    def get_info(self):
        output = super().get_info()
        output += "\nCurrent location: ("
        output += str(self.location_x)
        output += ","
        output += str(self.location_y)
        output += ")\nHP: "
        output += str(self.health)
        output += "\nAttack power: "
        output += str(self.attack)
        output += "\nExperience: "
        output += str(self.exp)
        return output