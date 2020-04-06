"""
    __init__.py
        - Imports Flask
        - Creates the app callable object
"""

from flask import Flask

app = Flask(__name__)

from project import views
from project import admin_views
