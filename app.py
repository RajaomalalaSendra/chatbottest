import json
from flask import Flask, request
from bot import Bot
PAGE_ACCESS_TOKEN = 'EAAEsSZCLLvZBEBALH9SU4xCLy69zKVCgTwIZBeWsyG3LEZAyEMlfZCVIQdgyFUYkmHoNiO2ZBzJv6hA9urNuiSorynWCYbW3fqxM4bg4uvWZAYM4zN94gLNP9JZBdDZAZAeKjUku0yCatDBiVvqKltLaQbmgBSH6ZApIJFxnvZC3DDLAtQZDZD'

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Webhook verification in this
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if token == 'n5T5yzuZWTaK/oE0+1spNcNEKBrmcd6vPvHBAJSNTE0=':
            return str(challenge)
        return "400"
    else:
        data = json.loads(request.data)
        messaging_events = data['entry'][0]['messaging']
        bot = Bot(PAGE_ACCESS_TOKEN)
        for message in messaging_events:
            user_id = message['sender']['id']
            # text_input = message['message'].get('text')
            # print("Message from: {} is: {}".format(user_id, text_input))
            bot.send_text_message(user_id, "Test....")
        return '200'

if __name__ == '__main__':
    app.run(debug=True)
