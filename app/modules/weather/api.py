from app.modules.weather.resources.base.Weather import Weather


def get_current_weather(**kwargs):
    local_weather = Weather(**kwargs)
    return local_weather.get_current_weather()


def get_forecast_weather(days, **kwargs):
    local_weather = Weather(**kwargs)
    return local_weather.get_forecast_weather(days)
