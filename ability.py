import random

class Ability:
    '''Contains a method to return the value of damage caused by attacking with an abiltiy'''
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        '''Calculates an ability's damage as a random number between 0 and its max damage'''
        random_value = random.randint(0, self.max_damage)
        return random_value

    
if __name__ == "__main__":
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())
