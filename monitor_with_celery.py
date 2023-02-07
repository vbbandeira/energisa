import re
import imaplib
import base64
from celery import Celery

app = Celery('monitor_with_celery',  broker='pyamqp://guest:guest@localhost:5672//',
             serializer='pickle')


def extract_data(email_body: str) -> str:
    match_name = re.search(r', ([A-Za-z0-9]+( [A-Za-z0-9]+)+)!', email_body)
    match_security_code = re.search(
        r'[\r\n]+([0-9])[\r\n]+([0-9])[\r\n]+([0-9])[\r\n]+([0-9])', email_body)

    if match_name and match_security_code:
        name = match_name.group(1)
        security_code = ''.join(match_security_code.groups())

        return name, security_code
    else:
        return None


@app.task
def monitor_inbox(username: str, password: str, subject: str) -> None:
    connection = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    connection.login(username, password)

    connection.select('inbox')
    connection.literal = base64.b64decode(subject).decode('utf-8')

    status, emails = connection.search('utf-8', 'UNSEEN SUBJECT')

    for email_id in emails[0].split():
        status, email_data = connection.fetch(email_id, '(RFC822)')
        email_body = email_data[0][1].decode('utf-8')

        data = extract_data(email_body)

        if data:
            process_email.apply_async((data), serializer='pickle')

        status, email_data = connection.store(email_id, '+FLAGS', '\\Seen')


@app.task
def process_email(data):
    name, security_code = data
    print(f'Name: {name}')
    print(f'Security Code: {security_code}')


USERNAME = 'exemplosolar@gmail.com'
PASSWORD = 'rcnenggouxpcnhbf'
SUBJECT = base64.b64encode(
    'Fwd: Código de segurança da Energisa'.encode('utf-8')).decode('utf-8')

monitor_inbox.apply_async((USERNAME, PASSWORD, SUBJECT), countdown=60)
