from character import getCharacter
from weapons import create_weapon
from random_loot_event import random_loot, random_event

def get_home():
  prompt = input("\nPlease select a function: \n (1) Add a Weapon: \n (2) View a Character: \n (3) Random Loot \n (4) Random Event \n>")
  if prompt == "1":
    create_weapon()
  elif prompt == "2":
    getCharacter()
  elif prompt == "3":
    random_loot()
  elif prompt == "4":
    random_event()
  else:
    get_home()

def return_bar():
  status = input("\nWould you like to continue? (y/n) \n>")
  if status == 'y' or status == 'Y':
    get_home()