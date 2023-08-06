from queue import Empty
from logging import getLogger
from threading import Thread
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from threading import Event
    from mail_office.models import EmailMessage
    from mail_office.queue_ import Queue


logger = getLogger(__name__)


class Postman(Thread):
    """
    Sender of queued messages (Worker).

    This is the only class in the application that interacts
    with email message instances.

    In fact, the job of this class is to use instance methods in the background.
    """

    def __init__(
        self,
        queue: "Queue",
        shutdown_event: "Event",
        delete_sent_messages: bool
    ) -> None:
        super().__init__()
        self.queue = queue
        self.shutdown_event = shutdown_event
        self.delete_sent_messages = delete_sent_messages

    def run(self) -> None:
        """
        Starts a cycle for sending messages.

        Note that the postman exits based on threading.Event and not
        on any magic value received from the queue.

        Firstly, this approach eliminates the need to clear the queue
        (in order to prioritize the magic value) and queue this magic
        value in the number corresponding to the number of postmen.

        Secondly, if the thread is made daemonic, then if the postman
        took a message from the queue and the program termination was caused,
        the postman will not have time to send the message, which will lead
        to the need to send this message at the next start.
        """
        while not self.shutdown_event.is_set():
            try:
                email_message: "EmailMessage" = self.queue.get(timeout=2)
                logger.info("received email message")
            except Empty:
                # It is perceived as the fact that no new messages have
                # appeared in the queue at the time "get" is called.
                continue

            self.send_message(email_message)

    def send_message(self, email_message: "EmailMessage") -> None:
        try:
            email_message.send()
            email_message.process_sent(self.delete_sent_messages)
            logger.info("email sent")
        except Exception as exc:
            logger.exception("lol", exc_info=exc)
            email_message.process_failed(exc)
