"""
enter virtual environment with

$ source venv/bin/activate

start flask with 

$ flask run

-------

send POST request with

{
	"santas": [
		{"name": "human 1", "email": "human1@email.com"},
		{"name": "human 2", "email": "human2@email.com"},
		{"name": "human 3", "email": "human3@email.com"},
		{"name": "human 4", "email": "human4@email.com"}
	],
	"message": "Dear {santa}, something"
}

"""
from flask import Flask, request, jsonify

from .generate_assignments import generate_assignments
import .settings

app = Flask(__name__)




@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        return post(request)
    return "<p>Send a POST request to this url to send emails</p>"

def post(request):
    data = request.get_json()
    santas = generate_assignments(data['santas'])
    return jsonify(assignments)
