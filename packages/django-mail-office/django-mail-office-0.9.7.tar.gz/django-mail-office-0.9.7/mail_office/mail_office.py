from logging import info
from threading import Event
from time import sleep
from typing import Optional

from mail_office.models import EmailMessage
from mail_office.postman import Postman
from mail_office.queue_ import Queue


class MailOffice:
    """
    This class is similar to a post office from the real world.

    The principle of operation is as follows:
    the user of the application creates an instance of the email message model,
    which, after creation, is located in the database. MailOffice retrieves from
    the database all instances created by the user and puts them in a queue,
    from which they are received and sent by postmen.
    """

    def __init__(
        self,
        min_queue_size: int,
        max_queue_size: int,
        delete_sent_messages: bool,
        new_messages_wait_time: int
    ) -> None:
        self.shutdown_event = Event()
        self.postman_threads: list[Postman] = []
        self.delete_sent_messages = delete_sent_messages

        self.queue = Queue()
        self.min_queue_size = min_queue_size
        self.max_queue_size = max_queue_size
        self.new_messages_wait_time = new_messages_wait_time

    def push_email_messages(self) -> Optional[int]:
        """
        Queues as many instances of the email message model as needed to
        reach the maximum number of objects in the queue (max_queue_size).

        Filling does not always happen. To retrieve objects from the database
        less often, filling begins when the number of messages in the queue at
        the time of the call is minimal (min_queue_size).

        The queue is constantly filled with objects, if the user has specified
        "min_queue_size = 0".
        """
        if (current_messages_count := self.queue.qsize) <= self.min_queue_size:
            quantity_to_fill = self.max_queue_size - current_messages_count

            if email_messages := EmailMessage.objects.choose_to_send(quantity_to_fill):
                for email_message in email_messages:
                    print("putted email message")
                    self.queue.put(email_message)

                return len(email_messages)

            sleep(self.new_messages_wait_time)

    def start_mailing(self, postmen_count: int) -> None:
        """
        Launches postmen and an endless loop, each iteration of
        which includes replenishing the queue with email messages.
        """
        self.start_postmen(postmen_count)

        while True:
            if pushed_count := self.push_email_messages():
                info(
                    "%d email messages pushed to the queue.",
                    pushed_count
                )

    def start_postmen(self, count: int) -> None:
        """
        Creates and launches postmen. In addition,
        adds them to the list so that later they can be stopped.
        """
        for _ in range(count):
            postman_thread = Postman(self.queue,
                                     self.shutdown_event,
                                     self.delete_sent_messages)
            postman_thread.start()
            self.postman_threads.append(postman_thread)

    def stop_postmen(self) -> None:
        """
        Signals through threading.Event
        to all postmen that it is time to exit.

        The reason why threading.Event is used is documented
        in the run method of the Postman.
        """
        self.shutdown_event.set()

        for postman_thread in self.postman_threads:
            postman_thread.join()