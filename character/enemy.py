from character.character import Character
class Enemy(Character):
    def __init__(self, name="default", lvl=0, description="default enemy", atk=1, exp=1, ASCII=":)"):
        super().__init__(name, lvl, description)
        self.attack = atk
        self.experience_value = exp
        self.ASCII = ASCII