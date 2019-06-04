import json
import os
import sys
from flask import Flask, request
from bot import Bot
from accessing import PAGE_ACCESS_TOKEN, VERIFY_TOKEN, FB_API_URL

app = Flask(__name__)

bot = Bot(PAGE_ACCESS_TOKEN)


@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Webhook verification in this
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if token == VERIFY_TOKEN:
            return str(challenge)
        return "400"
    else:
        data = json.loads(request.data)
        messaging_events = data['entry'][0]['messaging']
        for message in messaging_events:
            user_id = message['sender']['id']
            # text_input = message['message'].get('text')
            # print("Message from: {} is: {}".format(user_id, text_input))
            bot.send_text_message(user_id, "Test....")
        return '200'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
