import requests
import json


API_TOKEN = ''


class Weather:
    def __init__(self, **kwargs):
        global API_TOKEN
        self.api_token = str(API_TOKEN)
        self.base_url = kwargs['base_url'] if 'base_url' in kwargs else 'http://api.apixu.com'
        self.version = kwargs['version'] if 'version' in kwargs else 'v1'
        self.zipcode = kwargs['zipcode'] if 'zipcode' in kwargs else '06510'
        self.is_mock = kwargs['is_mock'] if 'is_mock' in kwargs else False

    def get_request_url(self, request_id):
        url = "%s/%s/%s" % (self.base_url, self.version, request_id)
        return url

    def get_forecast_weather(self, days=7):
        if self.is_mock:
            with open('app/modules/weather/examples/forecast.json', 'r') as forecast:
                return json.loads(forecast.read())
        headers = {'content-type': 'application/json'}
        params = {'key': self.api_token, 'days': days, 'q': self.zipcode}
        response = requests.get(self.get_request_url(request_id='forecast.json'), params=params, headers=headers)
        response.raise_for_status()
        return json.loads(response.content)

    def get_current_weather(self):
        if self.is_mock:
            with open('app/modules/weather/examples/current.json', 'r') as current:
                return json.loads(current.read())
        headers = {'content-type': 'application/json'}
        params = {'key': self.api_token, 'q': self.zipcode}
        response = requests.get(self.get_request_url(request_id='current.json'), params=params, headers=headers)
        response.raise_for_status()
        return json.loads(response.content)


if __name__ == '__main__':
    weather = Weather(is_mock=True)
    print(weather.get_forecast_weather())
