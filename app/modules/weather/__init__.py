from flask import Blueprint
from app.modules.weather import api
from app.modules.weather.resources.base import Weather

bp = Blueprint('weather', __name__)
