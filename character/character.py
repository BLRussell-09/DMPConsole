from home import home
import requests
import json

url = 'https://dungeonmastersapi20190214061000.azurewebsites.net/api/pc/'

def getUser(user_id):
  new_url = url + str(user_id)
  user = requests.get(new_url).json()
  user = user[0]
  name = user["name"]
  return name

def getCharacter():
  id = input("What is the id of the Character? ")
  id = int(id)
  new_url = url + str(id)
  user = requests.get(new_url).json()
  user = user[0]
  desc = user["description"]
  level = user["level"]
  name = user["name"]
  race = user["race"]["name"]
  hp = user["hit_points"]
  print(f"\nName: {name}: {desc}\n")
  print(f"Race: {race}\n")
  print(f"Level: {level}\n")
  print(f"Hit Points: {hp}\n")
  list_weapons(user["weapons"])
  list_skills(user["skills"])
  home.return_bar()

def list_weapons(weapons):
  print("Weapons: \n")
  for weapon in weapons:
    weapon_name = weapon["name"]
    weapon_desc = weapon["description"]
    print(f"  Name: {weapon_name}")
    print(f"  Description: {weapon_desc}\n")

def list_skills(skills):
  print("Skills: \n")
  for skill in skills:
    if skills[skill] == True:
      print(f" {skill}")