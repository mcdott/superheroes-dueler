import random
from ability import Ability
from armour import Armour 

class Hero:
  def __init__(self, name, starting_health=100):
    self.abilities = list()
    self.armour = list()
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health

  def add_ability(self, ability):
    self.abilities.append(ability)

  def attack(self):
    total_damage = 0
    for ability in self.abilities:
      total_damage += ability.attack()
    return total_damage

  def add_armour(self, armour):
    self.armour.append(armour)

  def defend(self):
    total_block = 0
    if len(self.armour) > 0 and self.current_health > 0:  
      for armour in self.armour:
        total_block += armour.block()
    return total_block



    
  def fight(self, opponent):
    random_num = random.randint(0, 99)
    opponents_chance_of_winning_percentage = opponent.current_health/(opponent.current_health + self.current_health) * 100

    # If the random number is less than the opponents chance of winning, the opponent wins
    if random_num < opponents_chance_of_winning_percentage:
      print(f"{opponent.name} defeats {self.name}!")
    else:
      print(f"{self.name} defeats {opponent.name}!")


if __name__ == "__main__":
    
    # my_hero = Hero("Grace Hopper", 200)
    # print(my_hero.name)
    # print(my_hero.current_health)

    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")

    # hero1.fight(hero2)

    debugging = Ability("Great Debuggin", 50)
    intelligence = Ability("Intelligence", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(debugging)
    hero.add_ability(intelligence)
    print(f'Attack: {hero.attack()}')

    persistence = Armour("Persistence", 75)
    self_confidence = Armour("Self-confidence", 50)
    hero.add_armour(persistence)
    hero.add_armour(self_confidence)
    print(f'Defence: {hero.defend()}')