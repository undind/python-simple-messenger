from datetime import datetime
from flask import Flask, request
import time

app = Flask(__name__)
messages = [
    {'username': 'John', 'time': time.time(), 'text': 'Hello!'},
    {'username': 'Merry', 'time': time.time(), 'text': 'Hello, John!'},
]
password_storage = {
    'John': '12345',
    'Merry': '54321'
}


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
    JSON {"username": str, "password": str, "text": str}
    username, text - непустые строки
    :return: {'ok': bool}
    """
    username = request.json['username']
    password = request.json['password']
    text = request.json['text']

    # First attempt for password is always valid
    if username not in password_storage:
        password_storage[username] = password

    # validate
    if not isinstance(username, str) or len(username) == 0:
        return {'ok', False}
    if not isinstance(text, str) or len(text) == 0:
        return {'ok', False}
    if password_storage[username] != password:
        return {'ok', False}

    # TODO
    messages.append({'username': username, 'time': time.time(), 'text': text})

    return {'ok': True}


@app.route("/messages")
def messages_method():
    """
    Param after - отметка времени после которой будут сообщения в результате
    :return: {'messages': [
        {'username': str, 'time': float, 'text': str},
        ...
    ]}
    """
    after = float(request.args['after'])
    filtered_messages = [message for message in messages if message['time'] > after]
    return {'messages': filtered_messages}


app.run()
