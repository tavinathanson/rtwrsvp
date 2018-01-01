from flask import Flask, request
from flask.json import jsonify
from six.moves.urllib.parse import unquote_plus
from werkzeug.datastructures import MultiDict

app = Flask(__name__)

@app.route('/')
def index():
    return 'rebeccaandtavi.com RSVP!'

@app.route('/rsvp', methods=['POST'])
def rsvp():
    data = request_dict(request.get_data())
    print("Data:")
    print(data)
    email = unquote_plus(data["email"])
    return email

def request_dict(data):
    return MultiDict([part.split("=") for part in data.split("&")])
