import imaplib
import re


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


def monitor_inbox(username: str, password: str, subject: str) -> None:
    connection = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    connection.login(username, password)

    while True:
        connection.select('inbox')
        connection.literal = subject

        status, emails = connection.search('utf-8', 'UNSEEN SUBJECT')

        for email_id in emails[0].split():
            status, email_data = connection.fetch(email_id, '(RFC822)')
            email_body = email_data[0][1].decode('utf-8')

            data = extract_data(email_body)

            if data:
                name, security_code = data
                print(f'Name: {name}')
                print(f'Security Code: {security_code}')
            else:
                print('Unable to find any name and security code in email')

            status, email_data = connection.store(email_id, '+FLAGS', '\\Seen')

    # connection.close()
    # connection.logout()


USERNAME = 'exemplosolar@gmail.com'
PASSWORD = 'rcnenggouxpcnhbf'
SUBJECT = 'Fwd: Código de segurança da Energisa'.encode('utf-8')

monitor_inbox(USERNAME, PASSWORD, SUBJECT)
