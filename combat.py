from character.player import Player
from character.enemy import Enemy
"""Handle combat between player and enemy entities."""
class Combat:
    def __init__(self, player, enemy):
        self.player_obj = player # store reference to player for access during fight
        self.enemy_obj = enemy # store reference to enemy for access during fight
        
    def turn(self, entity):
        if(type(entity) == Player):
            Player.take_turn()
        elif(type(entity) == Enemy):
            Enemy.take_turn()