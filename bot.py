import json
import requests

FACEBOOK_GRAPH_URL = "https://graph.facebook.com/v3.3/me/messages"


class Bot(object):
    """docstring for Bot"""

    def __init__(self, access_token, url_fb=FACEBOOK_GRAPH_URL):
        self.access_token = access_token
        self.url_fb = url_fb

    def send_text_message(self, psid, message, messaging_type="RESPONSE"):
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'messaging_type': messaging_type,
            'recipient': {'id': psid},
            'message': {'text': message}
        }
        params = {'access_token': self.access_token}
        response = requests.post(self.url_fb,
                                 headers=headers,
                                 params=params,
                                 data=json.dumps(data))
        print(response.content)
