from typing import TYPE_CHECKING

from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.core.mail import EmailMessage as EmailMessage_
from django.db import models
from django.db.transaction import atomic
from django.utils.module_loading import import_string
from django.utils.timezone import now

if TYPE_CHECKING:
    from django.template.backends.base import BaseEngine


template_backend_path = settings.TEMPLATES[0]["BACKEND"]
template_backend: "BaseEngine" = import_string(template_backend_path)


get_rendered_template_string = (
    lambda template_string, context:
    template_backend.from_string(template_string).render(context)
)


class EmailMessageManager(models.Manager):
    @atomic
    def reset_messages(self) -> None:
        """
        Allows to next start not ignore messages that have been selected
        for sending, but not sent due to the completion of the application.
        """
        self.select_for_update() \
            .filter(status=EmailMessage.Statuses.in_sending) \
            .update(status=EmailMessage.Statuses.new)

    @atomic
    def choose_to_send(self, count: int) -> models.QuerySet["EmailMessage"]:
        base_queryset = self.select_for_update().filter(
            status=EmailMessage.Statuses.new, send_time=now()
        )
        pks = list(
            base_queryset[:count].values_list('pk', flat=True)
        )
        messages_to_send = self.select_for_update().filter(id__in=pks)
        messages_to_send.update(status=EmailMessage.Statuses.in_sending)
        return messages_to_send


class EmailMessage(models.Model):
    class Statuses(models.TextChoices):
        new = "new"
        in_sending = "in_sending"
        canceled = "canceled"
        failed = "failed"
        sent = "sent"

    class Priorities(models.IntegerChoices):
        high = 1
        medium = 2
        low = 3

    status = models.CharField(
        max_length=10,
        choices=Statuses.choices,
        default=Statuses.new
    )

    priority = models.PositiveSmallIntegerField(
        choices=Priorities.choices,
        default=Priorities.high
    )

    subject = models.CharField(max_length=998, blank=True)

    plain_body = models.TextField(blank=True)

    fail_silently = models.BooleanField(default=False)

    to = ArrayField(models.EmailField(blank=True), blank=True)

    send_time = models.DateTimeField(default=now)

    objects = EmailMessageManager()

    class Meta:
        ordering = ("priority")

    # def get_django_email_message(self):
    #     kwargs = {
    #         "from_email": self.from_email,
    #         "to": self.to,
    #         "bcc": self.bcc,
    #         "headers": self.headers,
    #         "cc": self.cc,
    #         "reply_to": self.reply_to,
    #
    #         "subject": get_rendered_template_string(
    #             self.subject, self.context
    #         ),
    #         "body": get_rendered_template_string(
    #             self.plain_body, self.context
    #         )
    #     }
    #
    #     if html_body := get_rendered_template_string(
    #         self.html_body,
    #         self.context
    #     ):
    #         email_message = EmailMultiAlternatives(**kwargs)
    #         email_message.attach_alternative(html_body, "text/html")
    #     else:
    #         return EmailMessage_(**kwargs)
    #
    #     return email_message

    def send(self) -> None:
        print("sending email message")
        email_message = EmailMessage_(subject=self.subject, body=self.plain_body, to=self.to)
        email_message.send(self.fail_silently)

    def process_sent(self, need_to_delete: bool) -> None:
        if need_to_delete:
            print("message sent.deleting.")
            self.delete()
            return

        self.status = self.Statuses.sent
        self.save(update_fields=["status"])

    def process_failed(self, reason: Exception) -> None:
        pass
