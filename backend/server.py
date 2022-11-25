from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_message():
    name = request.args.get('name')
    msg = request.args.get('message')

    return f'<center><h2>{name}, {msg}</h2></center>'
