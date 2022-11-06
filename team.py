import random

class Team:
    '''
    Contains methods to update and print the list of heroes on a team, 
    and to battle against an opposing team 
    '''
    def __init__(self, name):
        self.name = name
        self.heroes =list()

    def add_hero(self, hero):
        '''Adds a hero to the list of heroes on the team'''
        self.heroes.append(hero)

    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        foundHero = False
        # loop through each hero in our list
        for hero in self.heroes:
            # if we find them, remove them from the list
            if hero.name == name:
                self.heroes.remove(hero)
            # set our indicator to True
                foundHero = True
        if not foundHero:
            return 0

    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        # Print heroes' names to the terminal one by one
        for hero in self.heroes:
            print(hero.name)

    def stats(self):
        '''Prints the team statistics'''
        for hero in self.heroes:
            if hero.deaths == 0:
                kd = hero.kills
            else:
                kd = hero.kills / hero.deaths
            print(f"{hero.name} Kill/Deaths:{kd}")

    def revive_heroes(self, health=100):
        ''' Resets all heroes' health to starting_health'''
        for hero in self.heroes:
            hero.current_health = health

    def attack(self, other_team):
        ''' Battles a team against an opposing team'''
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            # Randomly select a living hero from each team
            chosen_hero = random.choice(living_heroes)
            chosen_opponent = random.choice(living_opponents)
            chosen_hero.fight(chosen_opponent)
  
            # Update living_heroes and living_opponents to reflect the result of the fight
            if not chosen_hero.is_alive():
                living_heroes.remove(chosen_hero)
            if not chosen_opponent.is_alive():
                living_opponents.remove(chosen_opponent)

  


