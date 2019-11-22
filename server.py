from datetime import datetime
from flask import Flask, request
import time

app = Flask(__name__)
messages = [
    {'username': 'John', 'time': time.time(), 'text': 'Hello!'},
    {'username': 'Merry', 'time': time.time(), 'text': 'Hello, John!'},
]


@app.route("/")
def hello_method():
    return "Hello, World!"


@app.route("/status")
def status_method():
    return {
        'status': True,
        'datetime': datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    }


@app.route("/send", methods=['POST'])
def send_method():
    """
    JSON {"username": str, "text": str}
    username, text - непустые строки
    :return: {'ok': bool}
    """
    username = request.json['username']
    text = request.json['text']

    # validate
    if not isinstance(username, str) or len(username) == 0:
        return {'ok', False}
    if not isinstance(text, str) or len(text) == 0:
        return {'ok', False}

    # TODO
    messages.append({'username': username, 'time': datetime.now(), 'text': text})

    return {'ok': True}


@app.route("/messages")
def messages_method():
    """
    JSON {}
    :return: {'messages': [
        {'username': str, 'time': str, 'text': str},
        ...
    ]}
    """
    return {'messages': messages}


app.run()
