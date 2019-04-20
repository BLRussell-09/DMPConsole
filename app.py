import requests
import json
from home import get_home
from flask import Flask
import logging as logger
import auth

logger.basicConfig(level="DEBUG")
app = Flask(__name__)
app.route('/')

print("\nWelcome to the DMP Console App\n")
auth.sign_in()