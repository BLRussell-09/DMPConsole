import requests
import json
import home

loot_url = "https://dungeonmastersapi20190214061000.azurewebsites.net/api/loot"
event_url = "https://dungeonmastersapi20190214061000.azurewebsites.net/api/event"
def random_loot():
  loot = requests.get(loot_url).text
  print(f"\n{loot}\n")
  home.return_bar()

def random_event():
  event = requests.get(event_url).text
  print(f"\n{event}\n")
  home.return_bar()