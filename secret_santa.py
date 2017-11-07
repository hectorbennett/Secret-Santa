"""Secret Santa.

This program generates secret santas pairs and emails them to specified
accounts
"""
import random
import smtplib

SANTAS = {
    'Person 1': 'person1@email.com',
    'Person 2': 'person2@email.com',
    'Person 3': 'person3@mail.com',
    'etc': ''
}


def send_email(user, pwd, recipient, subject, body):
    """
    Sends an email with gmail.
    """

    message = """From: {user}\nTo: {recipient}\nSubject: {subject}\n\n{body}
    """.format(user=user, recipient=recipient, subject=subject, body=body)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(user, recipient, message)
        server.close()
        print('successfully sent the mail')
    except:
        print('failed to send mail')


def is_derangement(tuple_list):
    """
    Checks if a tuple list is a derangement, that is, if no pair is the same
    value twice. (i.e. no one is their own Secret Santa)
    """
    for i, j in tuple_list:
        if i == j:
            return False
    return True


def generate_assignments(santas):
    """
    Generates a list of tuples - santas and giftees.
    """
    santa_list = list(santas)
    giftee_list = list(santas)
    random.shuffle(giftee_list)
    return list(zip(santa_list, giftee_list))


while True:
    ASSIGNMENT_LIST = generate_assignments(SANTAS)
    if is_derangement(ASSIGNMENT_LIST):
        break


MESSAGE = """
Dear {santa},

You have been assigned {giftee} as your giftee.

Good luck, and merry Christmas

Love, Autosanta
Ho Ho Ho
xxx
"""

for santa, giftee in ASSIGNMENT_LIST:
    santa_email = SANTAS[santa]
    email_content = MESSAGE.format(santa=santa, giftee=giftee)

    if santa == 'Hector':
        send_email(
            INSERT_GMAIL_USERNAME_HERE,
            INSERT_GMAIL_PASSWORD_HERE,
            santa_email,
            'Secret Santa',
            email_content
        )
