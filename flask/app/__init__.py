"""
    __init__.py
        - Imports Flask
        - Creates the app callable object
"""

from flask import Flask

app = Flask(__name__)

from app import views
from app import admin_views
