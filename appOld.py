#!env/bin/python
import random
from flask import Flask, jsonify, request, abort
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True



mail = Mail(app)

@app.route('/', methods=['GET'])
def get():
    return "Send a POST request to this url to send emails. Hi, how are you"


@app.route('/', methods=['POST'])
def post():
    if not request.json:
        abort(400)
    print(request.json)
    print(jsonify(request.json))
    create_and_send_emails(request.json)
    # task = {
    #     'id': tasks[-1]['id'] + 1,
    #     'title': request.json['title'],
    #     'description': request.json.get('description', ""),
    #     'done': False
    # }
    # tasks.append(task)
    return jsonify({'hello': 'world'}), 201

def create_and_send_emails(data):
    santas = generate_assignments(data['santas'])

    for santa in santas:
        msg = Message('Hello', sender=app.config['MAIL_USERNAME'], recipients=[santa['email']])
        msg.body = data['email_message'].format(santa=santa['name'], giftee=santa['giftee'])
        # mail.send(msg)

def generate_assignments(santa_list):
    """
    Generates a list of valid pairs, santas and giftees.
    """
    santa_dicts = []
    while True:
        santa_dicts = assign_random_giftees(santa_list)
        if is_derangement(santa_dicts):
            break
    return santa_dicts

def assign_random_giftees(santa_list):
    """
    Creates a randomised list of pairs from a list of names.
    """
    giftee_list = [santa['name'] for santa in santa_list]
    random.shuffle(giftee_list)

    for i, giftee in enumerate(giftee_list):
        santa_list[i]['giftee'] = giftee

    return santa_list

def is_derangement(dict_list):
    """
    Checks if a list of 2-tuples is a derangement, that is, no santa is paired
    with themselves.
    """
    for santa_dict in dict_list:
        if santa_dict['name'] == santa_dict['giftee']:
            return False
    return True


if __name__ == '__main__':
    app.run(debug=True)