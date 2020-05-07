from flask import Flask


app = Flask(__name__)

@app.route('/')

def index():
    return 'Hello!'


@app.route('/kek')
def kek():
    return 'sada23!'