from django.core.mail import send_mail, BadHeaderError


def send_email(recipient_emails, sender_email, body, subject): 
    try:
        send_mail(subject, body, sender_email, recipient_emails)
        return True
    except BadHeaderError:
        return False
