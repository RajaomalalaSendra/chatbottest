import os
import sys
from flask import Flask, request
from pymessenger import Bot
from accessing import PAGE_ACCESS_TOKEN, VERIFY_TOKEN

app = Flask(__name__)


chatbottest = Bot(PAGE_ACCESS_TOKEN)


@app.route('/', methods=['GET'])
def verify():
    # Webhook verification in this
    if request.args.get('hub.mode') == 'subscribe' and request.args.get('hub.challenge'):
        if not request.args.get('hub.verify_token') == VERIFY_TOKEN:
            return "Verification taken mismatch", 403
        return request.args['hub.challenge'], 200
    return "Hello World", 200


@app.route('/', methods=['POST'])
def webhook():
    # webhook function for our app
    data = request.get_json()
    log(data)

    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging in entry['messaging']:
                # Get all the IDs
                sender_id = messaging['sender']['id']
                recipient_id = messaging['recipient']['id']
                # get the message
                if messaging.get('message'):
                    if 'text' in messaging['message']:
                        messagging_text = messaging['message']['text']
                    else:
                        messagging_text = 'no text for this.'
                    # Echo
                    response = messaging_text
                    bot.send_text_message(sender_id, response)

    return 'OK, man', 200


def log(data):
    print(data)
    sys.stdout.flush()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
