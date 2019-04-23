from authy import auth
from flask import Flask
import logging as logger

app = Flask(__name__)
app.route('/')

print("\nWelcome to the DMP Console App\n")
auth.sign_in()