

from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
# from telegram import Update, Bot
from telegram.ext import filters, CommandHandler, ApplicationBuilder, MessageHandler, ConversationHandler
from text import question_message,  reminder_message
from config import TOKEN, PILL_PROGRAMMING, timezone
from datetime import datetime, timedelta, time
from key import pill_list_key, pill_time_key
from botCommand import start, send_message, unknown, get_date,  check_reply, send_reminder, get_pill

import logging

log = logging.getLogger(__name__)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
type_datetime = type(time(0, 0))


class BotApplication:
    def __init__(self):
        self.application = ApplicationBuilder().token(TOKEN).build()
        self.get_date = CommandHandler('time', get_date)
        self.start_handler = CommandHandler('start', start)
        # self.echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
        self.default_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), check_reply)
        self.get_pill_handler = CommandHandler(['pill', 'pastilla', 'dosis', 'cuantas'], get_pill)
        self.unknown_handler = MessageHandler(filters.COMMAND, unknown)
        self.job_queue = self.application.job_queue

        # job_minute = self.job_queue.run_repeating(send_message, data="Salut", interval=10, first=2)

        # global value for the bot
        self.time_wait_answer = 60  # time in second
        self.a_question_is_pending = False
        self.received_valid_answer = False
        self.first_time_insisting = True
        self.insisting_task = None

        # config function
        self.config_questions()

        #
        self.activate_handler()

    def get_question(self, pill_list, is_reminder=False):
        """
        Method to get the question message and activate the different value
        """
        if is_reminder:
            message = reminder_message(' y '.join(pill_list)) + " \n" + str(datetime.now().strftime("%m/%d/%Y, %H:%M"))
        else:
            message = question_message(' y '.join(pill_list)) + " \n" + str(datetime.now().strftime("%m/%d/%Y, %H:%M"))
        self.received_valid_answer = False
        self.first_time_insisting = True  # reset first time insisting
        return message

    def config_questions(self):
        """
        Method to schedule the send of the question at a specific time
        """

        for pill_config in PILL_PROGRAMMING:
            time_value = pill_config[pill_time_key]
            log.info('date plan =' + str(time_value))
            log.info('current time zone : ' + str(time_value.strftime('%Z %z')))
            if time_value.strftime('%Z') != str(timezone):
                log.error("Error time zone do not match the specify one")
            self.job_queue.run_daily(send_message, data=[self.get_question(pill_list=pill_config[pill_list_key]),
                                                         pill_config[pill_list_key]],
                                     time=time_value, name="pill_reminder"+str(time_value.strftime("_%H:%M:%S_%Z")))
            for i in range(10):
                delta = 1

                if type(time_value) == type_datetime:
                    new_time = datetime.combine(datetime.today(), time_value) + timedelta(minutes=delta*(1+i))
                else:
                    new_time = datetime.combine(datetime.today(), time_value.timetz()) \
                               + timedelta(minutes=delta * (1 + i))
                self.job_queue.run_daily(send_reminder, data=self.get_question(pill_list=pill_config[pill_list_key],
                                                                               is_reminder=True),
                                         time=new_time.timetz(),
                                         name="pill_reminder_"+str(1+i)+str(new_time.strftime("_%H:%M:%S_%Z")))

    def activate_handler(self):
        # activate all the handler
        self.application.add_handler(self.start_handler)
        # self.application.add_handler(self.echo_handler)
        self.application.add_handler(self.get_date)
        self.application.add_handler(self.get_pill_handler)
        self.application.add_handler(self.default_handler)
        self.application.add_handler(self.unknown_handler)  # esto debe ser el ultimo handler
        self.application.run_polling()


if __name__ == '__main__':
    BotApplication()
