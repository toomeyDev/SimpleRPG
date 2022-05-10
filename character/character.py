class Character:
    def __init__(self, name="default", lvl=0, description="default character"):
        self.name = name
        self.lvl = lvl
        self.description = description

    def get_info(self):
        output = self.name 
        output += " level: " 
        output += str(self.lvl) 
        output += " description: "
        output += self.description
        return output

    def take_turn(self):
        """Execute turn during fight sequence."""
        print(f"It's {self.name}'s turn!\n")