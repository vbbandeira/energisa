# Energisa

To use Celery to handle the email processing task, you will need to set up a Celery worker and configure a message broker, such as Redis or RabbitMQ. 
The example I provided uses Redis as the message broker and starts the Celery worker with the command celery -A tasks worker --loglevel=info.

This script will schedule the check_email task to run every 60 seconds using Celery Beat, which is a built-in scheduler in Celery. 
This way, the script will constantly check for new emails with the subject "Fwd: Código de segurança da Energisa".
