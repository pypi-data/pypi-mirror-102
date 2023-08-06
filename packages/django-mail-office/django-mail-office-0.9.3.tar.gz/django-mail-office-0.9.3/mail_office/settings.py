from django.conf import settings


SETTINGS = {
    "POSTMEN_COUNT": 2,
    "DELETE_SENT_MESSAGES": False,

    "MIN_QUEUE_SIZE": 5,
    "MAX_QUEUE_SIZE": 20,
    "NEW_MESSAGES_WAIT_TIME": 2
}

SETTINGS.update(
    getattr(
        settings, "MAIL_OFFICE", {}
    )
)