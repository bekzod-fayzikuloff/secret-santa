from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.template import Context, loader


@shared_task
def email_notification(email_data):
    email_template = loader.get_template("email_notification.html").template
    email_context = Context(email_data)
    is_send = send_mail(
        subject=f"{email_data.get('first_name')}{email_data.get('last_name')}",
        message="",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email_data.get("email")],
        html_message=email_template.render(email_context),
    )
    return bool(is_send)
