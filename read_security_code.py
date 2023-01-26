# from celery import Celery
import email
import imaplib
import time

# Set the broker URL
# CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672//'

# Create a new Celery instance
# app = Celery('tasks', broker=CELERY_BROKER_URL)


# @app.task
def check_email():
    # Connect to the email server
    conn = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    conn.login("exemplosolar@gmail.com", "pimenta123")

    # Select the inbox folder
    conn.select("inbox")

    # Search for emails with the specific subject
    status, messages = conn.search(
        None, '(SUBJECT "Fwd: Código de segurança da Energisa")')

    # Iterate through the emails
    for msg_id in messages[0].split():
        # Get the email message
        status, msg_data = conn.fetch(msg_id, "(RFC822)")
        for response in msg_data:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])

                # Get the security code
                security_code = msg.get_payload()[0].get_payload()
                # Get the name from the email content
                name = msg.get_payload()[1].get_payload()
                print("Name:", name)
                print("Security Code:", security_code)

    # Disconnect from the email server
    conn.close()
    conn.logout()


# Schedule the check_email task to run every 60 seconds
# app.conf.beat_schedule = {
#     'check_email': {
#         'task': 'tasks.check_email',
#         'schedule': 1.0,
#     },
# }

# run the check_email function in an infinite loop
while True:
    check_email()
    time.sleep(30)  # Wait 30 seconds
