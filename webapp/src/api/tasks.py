from celery import shared_task
from django.core.mail import send_mail



@shared_task
def send_mail_new_user(mail_to):
    send_mail(
        "TESTING from tasks",
        "Here is the message from CELERY.",
        f"{mail_to}",
        ["y.negodenko@gmail.com"],
        fail_silently=False,
    )
    return True