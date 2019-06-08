import json
from flask import Flask, request
from bot import Bot
from accessing import PAGE_ACCESS_TOKEN, VERIFY_TOKEN
from list_answer import Answer

app = Flask(__name__)
bot_answer = Answer()


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
        bot = Bot(PAGE_ACCESS_TOKEN)
        for message in messaging_events:
            user_id = message['sender']['id']
            text_input = message['message'].get('text')
            answer = "I want to  answer you but I can't..."
            if text_input in bot_answer.greeting():
                answer = "welcome to my first bot test..."
            elif text_input in bot_answer.contact():
                answer = "contact BFV central is..."
            elif text_input in bot_answer.tarif():
                answer = "Tous les tarifs sont: ...."
            elif text_input in bot_answer.information():
                answer = "here is all the information about bfv..."
            elif text_input in bot_answer.urgence():
                answer = "This is an urgence from you as a user..."
            elif text_input in bot_answer.operation():
                answer = "This is the operation inside the bfv..."
            bot.send_text_message(user_id, answer)
        return '200'

if __name__ == '__main__':
    app.run(debug=True)
