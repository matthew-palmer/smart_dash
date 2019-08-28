from app.modules.weather.resources.base.Weather import Weather


class APIXUWeather(Weather):
    def __init__(self, **kwargs):
        super(APIXUWeather, self).__init__(**kwargs)
        self.base_url = 'http://api.apixu.com'
        self.version = kwargs['version'] if 'version' in kwargs else 'v1'
        self.forecast_request = 'forecast.json'
        self.current_request = 'current.json'
        self.uid = kwargs['uid'] if 'uid' in kwargs else 'apixu'
        self.params = {'key': self.api_token, 'q': self.zipcode, 'days': 7}


if __name__ == '__main__':
    weather = APIXUWeather(zipcode='06510', units='imperial', api_token='',
                           is_mock=True)
    print(weather.get_forecast_weather())
    print(weather.get_current_weather())
