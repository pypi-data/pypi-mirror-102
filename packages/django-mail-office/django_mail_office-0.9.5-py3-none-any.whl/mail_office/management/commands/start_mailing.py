from django.core.management.base import BaseCommand

from mail_office.mail_office import MailOffice
from mail_office.models import EmailMessage
from mail_office.settings import SETTINGS


class Command(BaseCommand):
    def handle(self, *args, **kwargs) -> None:
        postmen_count = SETTINGS.pop("POSTMEN_COUNT")

        mail_office = MailOffice(
            **{
                setting_name.lower(): setting_value
                for setting_name, setting_value in SETTINGS.items()
            }
        )

        EmailMessage.objects.reset_messages()

        self.stdout.write("Starting mailing.")
        try:
            mail_office.start_mailing(postmen_count)
        except (KeyboardInterrupt, SystemExit):
            self.stdout.write(
                "Received KeyboardInterrupt\SystemExit."
                "Completion of mailing."
            )
            mail_office.stop_postmen()