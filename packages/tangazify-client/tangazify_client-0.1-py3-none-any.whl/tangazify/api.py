import requests
from .config import TangazifyConfig

class TangazifyApi:
    def __init__(self, config=None):
        if config is None:
            config =TangazifyConfig()

        self.api_key = config.api_key
        self.secret_key = config.secret_key
        self.server_url = config.server_url

    def fetch_ads(self):
        headers = {
            'Api-Key': self.api_key,
            'Secret-Key': self.secret_key,
        }

        response = requests.get(f"{self.server_url}/hardware/fetch_ads/", headers=headers)

        if response.status_code == 200:
            try:
                ads = response.json()['ads']
                return ads
            except Exception as e:
                raise ValueError(f"Error decoding JSON: {e}")
        else:
            raise ValueError(f"Error: {response.status_code}")
