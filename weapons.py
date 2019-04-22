import json
import requests
import home
import character
weapon_url = 'https://dungeonmastersapi20190214061000.azurewebsites.net/api/weapons/add'

def create_weapon():
  weapon = {
    "name": "",
    "dice_count": 0,
    "damage_dice":  0,
    "description": "",
    "owner_id": 0
  }
  name = input("What is the weapon's name: ")
  weapon["name"] = name
  dice_count = input("Dice Count: ")
  weapon["dice_count"] = int(dice_count)
  damage_dice = input("Damge Dice: ")
  weapon["damage_dice"] = int(damage_dice)
  desc = input("Please give the weapon's description: ")
  weapon["description"] = desc
  add_owner(weapon)

def add_owner(weapon):
  owner_id = input("What is the owner's id? ")
  weapon["owner_id"] = int(owner_id)
  add_weapon(weapon)

def add_weapon(weapon):
  requests.post(weapon_url, json=weapon)
  owner_id = weapon["owner_id"]
  name = weapon["name"]
  user_name = character.getUser(owner_id)
  print(f"\n{name} has been added to {user_name}'s inventory!")
  home.return_bar()