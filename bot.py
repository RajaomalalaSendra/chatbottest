import json
import requests

FACEBOOK_GRAPH_URL = "https://graph.facebook.com/v3.3/me/"


class Bot(object):
    """docstring for Bot"""

    def __init__(self, access_token, api_url=FACEBOOK_GRAPH_URL):
        self.access_token = access_token
        self.api_url = api_url

    def send_text_message(self, PSID, message, messaging_type="RESPONSE"):
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'messaging_type': messaging_type,
            'recipient': {'id': PSID},
            'message': {'text': message}
        }
        params = {'access_token': self.access_token}
        self.api_url = self.api_url + 'messages'
        response = requests.post(self.api_url,
                                 headers=headers,
                                 params=params,
                                 data=json.dumps(data))
        print(response.content)
