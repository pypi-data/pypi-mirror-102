import ujson as json
import requests

from .lib.util import objects, exceptions


class Client():
    def __init__(self, token):
        self.api = "https://botdash.pro/api/v1"
        self.token = token;

    def get_value(self, guildId, value):
        response = requests.get(f"{self.api}/retrieve/{self.token}/{value}/{guildId}")
        if response.status_code != 200: raise exceptions.CheckException(json.loads(response.text))
        else: return objects.Value(json.loads(response.text))