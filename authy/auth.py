import pyrebase
from home import get_home
from authy import config

firebase = pyrebase.initialize_app(config.config)
auth = firebase.auth()

def sign_in():
  email = input("Please enter your email\n")
  password = input("Please enter your password\n")
  user = auth.sign_in_with_email_and_password(email, password)
  if user:
    get_home()
  else:
    exit()