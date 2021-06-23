from flask_mail import Mail, Message
from app import app

DEFAULT_MESSAGE = """
Dear {santa},

You have been assigned {giftee} as your giftee.

Good luck, and merry Christmas

Love, Autosanta
Ho Ho Ho
xxx
"""

mail = Mail(app)

app.config['MAIL_SERVER'] = settings.MAIL_SERVER
app.config['MAIL_PORT'] = settings.MAIL_PORT
app.config['MAIL_USE_TLS'] = settings.MAIL_USE_TLS
app.config['MAIL_USE_SSL'] = settings.MAIL_USE_SSL
app.config['MAIL_USERNAME'] = settings.MAIL_USERNAME
app.config['MAIL_PASSWORD'] = settings.MAIL_PASSWORD

# def send_email(
#         message_template=DEFAULT_MESSAGE,
#         santa_email=None,
#         santa_name=None,
#         giftee_name=None,
#     ):
#     msg = Message('Hello', sender=app.config['MAIL_USERNAME'], recipients=[santa['email']])
#     msg.body = message_template.format(santa=santa_name, giftee=giftee_name)
#     return mail.send(msg)


def send_email(message, recipient):