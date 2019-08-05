from flask import Blueprint, current_app, render_template
from app.resource.cache import cache

from .api import *

weather_blueprint = Blueprint('weather', __name__, url_prefix="/weather", template_folder='templates')


@weather_blueprint.route('/')
# @cache.cached(timeout=2592)
def get_weather_current():
    current_weather = get_current_weather(base_url=current_app.config['W_BASE_URL'],
                                          version=current_app.config['W_VERSION'],
                                          zipcode=current_app.config['W_ZIPCODE'],
                                          is_mock=current_app.config['IS_MOCK'])
    print(current_weather)
    return render_template("current_weather.html", location=current_weather['location'], current=current_weather['current'])


@weather_blueprint.route('/forecast')
# @cache.cached(timeout=2592)
def get_weather_forecast():
    forecast_weather = get_forecast_weather(7, base_url=current_app.config['W_BASE_URL'],
                                            version=current_app.config['W_VERSION'],
                                            zipcode=current_app.config['W_ZIPCODE'],
                                            is_mock=current_app.config['IS_MOCK'])
    print(forecast_weather)
    return render_template("forecast.html", forecast=forecast_weather['forecast']['forecastday'],
                           alerts=forecast_weather['alert'],
                           location=forecast_weather['location'])
