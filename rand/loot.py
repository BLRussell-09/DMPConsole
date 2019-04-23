from home import home
import requests
import json

loot_url = "https://dungeonmastersapi20190214061000.azurewebsites.net/api/loot"
def random_loot():
  loot = requests.get(loot_url).text
  print(f"\n{loot}\n")
  home.return_bar()