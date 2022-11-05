import random
from ability import Ability

class Weapon(Ability):
    def attack(self):
        # A weapon's damage is a random number between half of its max damage and its max damage
        half_max_damage = self.max_damage//2
        random_value = random.randint(half_max_damage, self.max_damage)
        return random_value

