import random
from ability import Ability

class Weapon(Ability):
    '''Contains a method to return the value of damage caused by attacking with a weapon'''
    def attack(self):
        '''Calculates a weapon's damage as a random number between half of its max damage and its max damage'''
        half_max_damage = self.max_damage//2
        random_value = random.randint(half_max_damage, self.max_damage)
        return random_value

