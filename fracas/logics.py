
import smtplib
import datetime
import random
import string

def get_random_key(limit=None, number=False):
    if not limit:
        limit = 64
    if number:
        return ''.join(random.choice(string.digits) for x in range(limit))
    else:
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(limit))


def sendEmail(sender, recipient, subject, body):

    FROM = sender
    TO = recipient
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, TO, SUBJECT, TEXT)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login('mahinmaja5790@gmail.com', 'maja5790')
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except:
        print("failed to send mail")
