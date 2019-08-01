from flask import Blueprint

bp = Blueprint('weather', __name__)

from app.modules.weather import api
