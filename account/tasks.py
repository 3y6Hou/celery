from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_activation_code(email, activation_code):
    activation_link = f'http://127.0.0.1:8000/account/activate/{activation_code}'
    message = f'Нажми на ссылку, для активации\n{activation_link}'
    send_mail('Activate account', message, 'ruslan883888@gmail.com', [email])


