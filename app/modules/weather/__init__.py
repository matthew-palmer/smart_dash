from flask import Blueprint
from app.modules.weather import api

bp = Blueprint('weather', __name__)
