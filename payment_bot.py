from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = 8117246169:AAESfMHEFdkF-EAkKVZVIqpMjpK56vPbBBA
CHAT_ID = 7021183974

@app.route('/freekassa', methods=['GET', 'POST'])
def freekassa_notify():
    message = f"Платеж прошёл! Параметры: {request.args.to_dict()}"
    requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", params={
        'chat_id': CHAT_ID,
        'text': message
    })
    return 'OK', 200