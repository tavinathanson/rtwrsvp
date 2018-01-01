from flask import Flask, request
from flask.json import jsonify
from six.moves.urllib.parse import unquote_plus

app = Flask(__name__)

@app.route('/')
def index():
    return 'rebeccaandtavi.com RSVP!'

@app.route('/rsvp', methods=['POST'])
def rsvp():
    email = unquote_plus(request.form["email"])
    return email
