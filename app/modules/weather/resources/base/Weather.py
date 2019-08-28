import requests
import json


class Weather:
    def __init__(self, api_token='', **kwargs):
        self.api_token = api_token
        self.base_url = kwargs['base_url'] if 'base_url' in kwargs else ''
        self.version = kwargs['version'] if 'version' in kwargs else ''
        self.zipcode = kwargs['zipcode']
        self.is_mock = kwargs['is_mock'] if 'is_mock' in kwargs else False
        self.forecast_request = ''
        self.current_request = ''
        self.uid = ''
        self.headers = {'content-type': 'application/json'}
        self.params = {}

    def get_request_url(self, request_id):
        url = "%s/%s/%s" % (self.base_url, self.version, request_id)
        return url

    def get_forecast_weather(self):
        if self.is_mock:
            with open('app/modules/weather/examples/%s-forecast.json' % self.uid, 'r') as forecast:
                return json.loads(forecast.read())
        response = requests.get(self.get_request_url(request_id=self.forecast_request),
                                params=self.params, headers=self.headers)
        response.raise_for_status()
        return json.loads(response.content)

    def get_current_weather(self):
        if self.is_mock:
            with open('app/modules/weather/examples/%s-current.json' % self.uid, 'r') as current:
                return json.loads(current.read())
        response = requests.get(self.get_request_url(request_id=self.current_request),
                                params=self.params, headers=self.headers)
        response.raise_for_status()
        return json.loads(response.content)

