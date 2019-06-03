import os
import sys
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def verify():
    # Webhook verification in this
    if request.args.get('hub.mode') == 'subscribe' and request.args.get('hub.challenge'):
        if not request.args.get('hub.verify_token') == 'n5T5yzuZWTaK/oE0+1spNcNEKBrmcd6vPvHBAJSNTE0=':
            return "Verification taken mismatch", 403
        return request.args['hub.challenge'], 200
    return "Hello World", 200


@app.route('/', methods=['POST'])
def webhook():
    # webhook function for our app
    data = request.get_json()
    log(data)
    return 'OK, man', 200


def log(data):
    print(data)
    sys.stdout.flush()

if __name__ == '__main__':
    app.run(debug=True, port=80)
