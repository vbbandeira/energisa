import imaplib
import time
import re

username = 'exemplosolar@gmail.com'
password = 'rcnenggouxpcnhbf'
subject = 'Fwd: Código de segurança da Energisa'.encode('utf-8')
regex_match_name = r'Ol=C3=A1, ([A-Za-z0-9]+( [A-Za-z0-9]+)+)!'
regex_match_security_code = r'[\r\n]+([0-9])[\r\n]+([0-9])[\r\n]+([0-9])[\r\n]+([0-9])'


def check_email():
    connection = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    connection.login(username, password)

    connection.select('inbox')
    connection.literal = subject

    status, emails = connection.search(
        'utf-8', 'SUBJECT')

    for email_id in emails[0].split():
        status, email_data = connection.fetch(email_id, '(RFC822)')
        email_body = email_data[0][1].decode('utf-8')

        match_name = re.search(regex_match_name, email_body)
        match_security_code = re.search(regex_match_security_code, email_body)

        if match_name and match_security_code:
            name = match_name.group(1)
            security_code = match_security_code.group(1, 2, 3, 4)
            print(f'Name: {name}')
            print(f'Security Code: {security_code}')
        else:
            print('Unable to find name and security code in email.')

    connection.close()
    connection.logout()


# run the check_email function in an infinite loop
while True:
    check_email()
    time.sleep(30)  # Wait 30 seconds
