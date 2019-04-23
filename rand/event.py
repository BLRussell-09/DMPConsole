from home import home
import requests
import json

event_url = "https://dungeonmastersapi20190214061000.azurewebsites.net/api/event"
def random_event():
  event = requests.get(event_url).text
  print(f"\n{event}\n")
  home.return_bar()