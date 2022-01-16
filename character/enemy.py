from character.character import Character
class Enemy(Character):
    def __init__(self, name="default", lvl=0, description="default enemy", hp=10, atk=1, exp=1, ASCII=":)"):
        super().__init__(name, lvl, description)
        self.attack = atk # multiplier used to calculate damage to player
        self.health = hp # amount of damage the enemy can take before defeat
        self.experience_value = exp # value in EXP this enemy gives to the player
        self.ASCII = ASCII # ASCII image art for this enemy

    def attack(self, dmg=2):
        """default attack with optional damage param"""
        print("Enemy used attack!")
        damage = self.attack * 1
        return damage # damage value, return to use adjusting player stats

    def get_hp(self):
        return self.health

    def set_hp(self, value):
        self.health = value

    def subtract_hp(self, amt):
        self.health -= amt

    def add_hp(self, amt):
        self.health += amt

    def __str__(self):
        output = self.name
        output +=f":\n"
        output +=self.description
        output +="\n"
        output += self.ASCII
        output += "\nHP: "
        output += str(self.health)
        output += "\nAttack power: "
        output += str(self.attack)
        return output