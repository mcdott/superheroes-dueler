from ability import Ability
from weapon import Weapon
from armour import Armour
from hero import Hero
from team import Team

class Arena:
  def __init__(self):
    '''Instantiate properties
        team_one: None
        team_two: None
    '''
    self.team_one = Team('Team One')
    self.team_two = Team('Team Two')

  def create_ability(self):
    '''Prompt for Ability information.
      return Ability with values from user Input
    '''
    name = input("What is the ability name?: ")
    max_damage = int(input("What is the max damage of the ability?: "))

    return Ability(name, max_damage)

  def create_weapon(self):
    '''Prompt user for Weapon information
        return Weapon with values from user input.
    '''
    name = input("What is the weapon name?: ")
    max_damage = int(input("What is the max damage of the weapon?: "))

    return Weapon (name, max_damage)

  def create_armour(self):
    '''Prompt user for Armour information
      return Armour with values from user input.
    '''
    name = input("What is the name of the piece of armour?: ")
    max_block = int(input("What is the max block of the piece of armour?: "))

    return Armour (name, max_block)

  def create_hero(self):
    '''Prompt user for Hero information
      return Hero with values from user input.
    '''
    hero_name = input("Hero's name: ")
    hero = Hero(hero_name)
    add_item = None
    while add_item != "4":
      add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armour\n[4] Done adding items\n\nYour choice: ")
      if add_item == "1":
        ability = self.create_ability()
        hero.add_ability(ability)
      elif add_item == "2":
        weapon = self.create_weapon()
        hero.add_weapon(weapon)
      elif add_item == "3":
        armour = self.create_armour()
        hero.add_armour(armour)

    return hero

  def build_team_one(self):
    '''Prompt the user to build team_one '''
    num_of_team_members = int(input("How many members would you like on Team One?: \n"))
    for i in range(num_of_team_members):
      hero = self.create_hero()
      self.team_one.add_hero(hero)

  def build_team_two(self):
    '''Prompt the user to build team_two'''
    num_of_team_members = int(input("How many members would you like on Team Two?: \n"))
    for i in range(num_of_team_members):
      hero = self.create_hero()
      self.team_two.add_hero(hero)

  def team_battle(self):
    '''Battle team_one and team_two together.'''
    self.team_one.attack(self.team_two)

  def show_stats(self):
    '''Prints team statistics to terminal.'''
    print("\n")
    print(self.team_one.name + " statistics: ")
    self.team_one.stats()
    print("\n")
    print(self.team_two.name + " statistics: ")
    self.team_two.stats()
    print("\n")

    # Calculate and display the average K/D for Team One
    team_kills = 0
    team_deaths = 0
    for hero in self.team_one.heroes:
        team_kills += hero.kills
        team_deaths += hero.deaths
    if team_deaths == 0:
        team_deaths = 1
    print(self.team_one.name + " average K/D was: " + str(team_kills/team_deaths))

    # Calculate and display the average K/D for Team Two
    team_kills = 0
    team_deaths = 0
    for hero in self.team_two.heroes:
        team_kills += hero.kills
        team_deaths += hero.deaths
    if team_deaths == 0:
        team_deaths = 1
    print(self.team_two.name + " average K/D was: " + str(team_kills/team_deaths))
   

    # List the heroes from Team One that survived
    for hero in self.team_one.heroes:
        if hero.deaths == 0:
            print("survived from " + self.team_one.name + ": " + hero.name)

    # List the heroes from Team Two that survived
    for hero in self.team_two.heroes:
        if hero.deaths == 0:
            print("survived from " + self.team_two.name + ": " + hero.name)
    

if __name__ == "__main__":
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()