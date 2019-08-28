from app.modules.weather.resources.base.Weather import Weather


class OpenWeather(Weather):
    def __init__(self, api_token='', **kwargs):
        super(OpenWeather, self).__init__(**kwargs)
        self.api_token = api_token
        self.base_url = 'https://api.openweathermap.org/data'
        self.version = kwargs['version'] if 'version' in kwargs else '2.5'
        self.units = kwargs['units']
        self.forecast_request = 'forecast'
        self.current_request = 'current'
        self.uid = kwargs['uid'] if 'uid' in kwargs else 'openweather'
        self.params = {'APPID': self.api_token, 'zip': self.zipcode, 'units': self.units}


if __name__ == '__main__':
    weather = OpenWeather(zipcode='06510', units='imperial', api_token='',
                          is_mock=True)
    print(weather.get_forecast_weather())
