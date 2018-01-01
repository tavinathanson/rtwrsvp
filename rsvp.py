from flask import Flask, request
from flask.json import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'rebeccaandtavi.com RSVP!'

@app.route('/rsvp', methods=['POST'])
def rsvp():
    email = request.form["email"]
    return email
