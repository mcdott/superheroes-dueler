import random
from ability import Ability
from armour import Armour 
from weapon import Weapon

class Hero:
  def __init__(self, name, starting_health=100):
    self.abilities = list()
    self.armour = list()
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health

  def add_ability(self, ability):
    self.abilities.append(ability)

  # Weapons are also counted as abilities
  def add_weapon(self, weapon):
    self.abilities.append(weapon)


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

  def take_damage(self, damage):
    defence = self.defend()
    # If the damage is greater than the defence, subtract the net damage from current health
    if damage > defence:
      self.current_health -= damage - defence

  def is_alive(self):
    if self.current_health > 0:
      return True
    else:
      return False

  def fight(self, opponent):
    if len(self.abilities) == 0 and len(opponent.abilities) == 0:
      print("Draw")
    else:
      while self.current_health > 0 and opponent.current_health > 0:
        # Each fighter attacks and each fighter takes damage
        damage_to_opponent = self.attack()
        opponent.take_damage(damage_to_opponent)
        damage_to_self = opponent.attack()
        self.take_damage(damage_to_self)

        # If at least one player has died, print the outcome of the fight
        if self.current_health <= 0 and opponent.current_health <= 0:
          print("Draw")
        elif opponent.current_health <= 0:
          print(f'{self.name} won!')
        elif self.current_health <= 0:
          print(f'{opponent.name} won!')


if __name__ == "__main__":

    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
   