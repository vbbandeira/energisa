import imaplib
import email
import time

username = "exemplosolar@gmail.com"
password = "rcnenggouxpcnhbf"
subject = "Fwd: Código de segurança da Energisa".encode('utf-8')


def check_email():
    # Connect to the email server
    connection = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    connection.login(username, password)

    # Select the inbox folder
    connection.select("inbox")
    connection.literal = subject

    status, messages = connection.search(
        'utf-8', 'SUBJECT')

    for msg_id in messages[0].split():
        status, msg_data = connection.fetch(msg_id, "(RFC822)")
        for response in msg_data:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                security_code = msg.get_payload()[0].get_payload()
                name = msg.get_payload()[1].get_payload()

                print("Name:", name)
                print("Security Code:", security_code)

    connection.close()
    connection.logout()


# run the check_email function in an infinite loop
while True:
    check_email()
    time.sleep(30)  # Wait 30 seconds
