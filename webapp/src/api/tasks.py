from celery import shared_task
from django.core.mail import send_mail

# Задача для Celery: отправка email-подтверждения

@shared_task
def send_mail_new_user(mail_to):
    send_mail(
        "TESTING Celery+Docker+Redis_APP",
        "Here is the message.",
        "y.negodenko@gmail.com",
        [f"{mail_to}"],
        fail_silently=False,
    )