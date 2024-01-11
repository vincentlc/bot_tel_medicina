from text import reply_valid, celebrate_message, reply_invalid_message
import logging

log = logging.getLogger(__name__)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


def check_message_ok(message):
    """Return the message to send and the status."""
    if message in reply_valid:
        return celebrate_message, True
    else:
        return reply_invalid_message, False


class ReaderActivation:
    def __init__(self):
        self.waiting_for_reply = False

    def get_if_waiting_rely(self):
        return self.waiting_for_reply

    def toggle_wait_reply(self, status):
        if isinstance(status, bool):
            self.waiting_for_reply=status
        else:
            log.error("the toggle value is not valid %s", status)