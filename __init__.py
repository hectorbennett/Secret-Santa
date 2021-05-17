"""

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

from generate_assignments import generate_assignments

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        return post(request)
    return "<p>Hello, World!</p>"

def post(request):
    data = request.get_json()
    assignments = generate_assignments(data['santas'])
    print(assignments)
    return jsonify(assignments)
    # return "Sent emails!"
