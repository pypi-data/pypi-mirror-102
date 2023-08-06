from typing import TYPE_CHECKING

from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.core.mail import EmailMessage as EmailMessage_, EmailMultiAlternatives
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
    def get_queryset(self) -> models.QuerySet["EmailMessage"]:
        return models.QuerySet(self.model, using=self._db)

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
    def choose_to_send(self, quantity: int) -> models.QuerySet["EmailMessage"]:
        sending_messages = self.filter(
            status=EmailMessage.Statuses.new,
            send_time__lte=now()
        )
        messages_to_send = self.get_queryset().select_for_update().filter(
            id__in=list(
                sending_messages[:quantity].values_list("pk", flat=True)
            )
        )
        messages_to_send.update(status=EmailMessage.Statuses.in_sending)
        return messages_to_send


class EmailMessageContentParts(models.Model):
    subject = models.CharField(max_length=998, blank=True)
    plain_body = models.TextField(blank=True)
    html_body = models.TextField(blank=True)

    class Meta:
        abstract = True


class EmailMessageTemplate(EmailMessageContentParts):
    name = models.CharField(max_length=100)


class EmailMessage(EmailMessageContentParts):
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
        default=Statuses.new,
        editable=False
    )
    priority = models.PositiveSmallIntegerField(
        choices=Priorities.choices,
        default=Priorities.high
    )
    template = models.ForeignKey(
        EmailMessageTemplate,
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    name = models.CharField(max_length=100)

    retries_number = models.PositiveSmallIntegerField(default=0)

    max_retries_number = models.PositiveSmallIntegerField(default=1)

    retry_delay = models.PositiveIntegerField(default=900)

    from_email = models.EmailField(blank=True)

    fail_silently = models.BooleanField(default=False)

    reply_to = ArrayField(models.EmailField(blank=True), blank=True)

    to = ArrayField(models.EmailField(blank=True), blank=True)

    cc = ArrayField(models.EmailField(blank=True), blank=True)

    bcc = ArrayField(models.EmailField(blank=True), blank=True)

    headers = models.JSONField(blank=True)

    context = models.JSONField(blank=True)

    created_at = models.DateTimeField(default=now)

    send_time = models.DateTimeField(default=now)

    objects = EmailMessageManager()

    class Meta:
        ordering = ("priority", "created_at")

    def get_django_email_message(self):
        content_parts_container = self if self.template is None else self.template

        kwargs = {
            "from_email": self.from_email,
            "to": self.to,
            "bcc": self.bcc,
            "headers": self.headers,
            "cc": self.cc,
            "reply_to": self.reply_to,

            "subject": get_rendered_template_string(
                content_parts_container.subject, self.context
            ),
            "body": get_rendered_template_string(
                content_parts_container.plain_body, self.context
            )
        }

        if html_body := get_rendered_template_string(
            content_parts_container.html_body,
            self.context
        ):
            email_message = EmailMultiAlternatives(**kwargs)
            email_message.attach_alternative(html_body, "text/html")
        else:
            return EmailMessage_(**kwargs)

        return email_message

    def send(self) -> None:
        self.get_django_email_message().send(self.fail_silently)

    def process_sent(self, need_to_delete: bool) -> None:
        if need_to_delete:
            self.delete()
            return

        self.status = self.Statuses.sent
        self.save(update_fields=["status"])

    def process_failed(self, reason: Exception) -> None:
        pass
