import random

class Armour:
    '''Contains a method to return the value of the protection caused by using a block'''
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        '''Calculates a block's protection as a random number between 0 and its max block'''
        random_value = random.randint(0, self.max_block)
        return random_value

if __name__ == "__main__":
  armour = Armour("Debugging Shield", 10)
  print(armour.name)
  print(armour.block())