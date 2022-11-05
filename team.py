class Team:
    def __init__(self, name):
        self.name = name
        self.heroes =list()

    def add_hero(self, hero):
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


