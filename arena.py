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

  def average_kills_over_deaths(self, team):
    '''Calculates the average k/d for a given team'''
    team_kills = 0
    team_deaths = 0
    for hero in team.heroes:
        team_kills += hero.kills
        team_deaths += hero.deaths
    if team_deaths == 0:
        team_deaths = 1
    team_kills_over_deaths = round(team_kills/team_deaths, 2)
    return (f'{team.name} average K/D was: {team_kills_over_deaths}')

  def print_surviving_hero_list(self, team_name, heroes):
    '''Print a list of the heroes on a team who survived'''
    for hero in heroes:
      if hero.deaths == 0:
        print("survived from " + team_name + ": " + hero.name)

  def show_stats(self):
    '''Prints team statistics to terminal.'''
    print("\n")
    print(self.team_one.name + " statistics: ")
    self.team_one.stats()
    print("\n")
    print(self.team_two.name + " statistics: ")
    self.team_two.stats()
    print("\n")
    print(self.average_kills_over_deaths(self.team_one))
    print(self.average_kills_over_deaths(self.team_two))
    self.print_surviving_hero_list(self.team_one.name, self.team_one.heroes)
    self.print_surviving_hero_list(self.team_two.name, self.team_two.heroes)

if __name__ == "__main__":
  game_is_running = True

  # Instantiate Game Arena
  arena = Arena()

  #Build Teams
  arena.build_team_one()
  arena.build_team_two()

  while game_is_running:

      arena.team_battle()
      arena.show_stats()
      play_again = input("Play Again? Y or N: ")

      #Check for Player Input
      if play_again.lower() == "n":
          game_is_running = False

      else:
          #Revive heroes to play again
          arena.team_one.revive_heroes()
          arena.team_two.revive_heroes()