import random

class Hero:
  def __init__(self, name, starting_health=100):
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health

    
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

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

    hero1.fight(hero2)