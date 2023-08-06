from django.contrib.admin import site

from mail_office.models import EmailMessage


site.register(EmailMessage)