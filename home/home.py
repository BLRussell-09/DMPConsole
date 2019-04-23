from character import character
from rand import loot, event
from character import weapons

def get_home():
  prompt = input("\nPlease select a function: \n (1) Add a Weapon: \n (2) View a Character: \n (3) Random Loot \n (4) Random Event \n>")
  if prompt == "1":
    weapons.create_weapon()
  elif prompt == "2":
    character.getCharacter()
  elif prompt == "3":
    loot.random_loot()
  elif prompt == "4":
    event.random_event()
  else:
    get_home()

def return_bar():
  status = input("\nWould you like to return to the main menu? (y/n) \n>")
  if status == 'y' or status == 'Y':
    get_home()