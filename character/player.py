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

    def get_x_coord(self):
        return self.location_x

    def get_y_coord(self):
        return self.location_y

    def get_coordinates(self):
        """Return the player character's current X/Y coordinates."""
        output = []
        output.append(self.location_x)
        output.append(self.location_y)
        return output

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

    def change_location(self, direction):
        """Move the player in the direction specified."""
        if(direction.lower() == "left"):
            print("Going left...\n")
            self.location_x -= 1
        elif(direction.lower() == "right"):
            print("Going right...\n")
            self.location_x += 1
        elif(direction.lower() == "up"):
            print("Going up...\n")
            self.location_y -= 1
        elif(direction.lower() == "down"):
            print("Going down...\n")
            self.location_y += 1