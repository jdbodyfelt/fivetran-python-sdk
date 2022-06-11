import os
import requests
from requests.auth import HTTPBasicAuth

class Auth:
    '''
    Fivetran Authentication Base Class
    '''
    def __init__(
        self, 
        api_key: str = os.getenv('FIVETRAN_API_KEY'), 
        api_secret: str = os.getenv('FIVETRAN_API_SECRET'),
        base_url: str = 'https://api.fivetran.com/v1',
    ):
        self.base_url = base_url
        if api_key is None or api_secret is None:
            raise ValueError('FIVETRAN_API_KEY/FIVETRAN_API_SECRET env variables missing.')
        self.auth = {
            'code': HTTPBasicAuth(api_key, api_secret), 
            'header': {'Authorization': f'Basic {api_key}', 'Content-Type': 'application/json'}
        }

    def url_(self, route: str):
        return f'{self.base_url}/{route}'

    def get(self, route: str, params: dict = None):
        response = requests.get(self.url_(route), params=params, headers=self.auth['header'], auth=self.auth['code'])
        return response.json()
        
    def post(self, route: str, data: dict = None):
        response = requests.post(self.url_(route), data=data, headers=self.auth['header'], auth=self.auth['code'])
        return response.json()

    def patch(self, route: str, data: dict = None):
        response = requests.patch(self.url_(route), data=data, headers=self.auth['header'], auth=self.auth['code'])
        return response.json()

    def delete(self, route: str):
        response = requests.delete(self.url_(route), headers=self.auth['header'], auth=self.auth['code'])
        return response.json()
    