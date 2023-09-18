

import asyncio
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
from telegram.ext import filters, Application, CommandHandler, ContextTypes, ApplicationBuilder, MessageHandler
from text import question_message, reply_valid, celebrate_message, reply_invalid_message, \
    insisting_message, reply_invalid_command, reminder_message
from config import TOKEN, CHAT_ID, PILL_PROGRAMMING
from datetime import datetime, timedelta, time
from key import pill_list_key, pill_quantity_key, pill_time_key
from botCommand import start, send_message, unknown, get_date, echo, check_reply, send_reminder

import logging

log = logging.getLogger(__name__)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


class BotApplication:
    def __init__(self):
        self.application = ApplicationBuilder().token(TOKEN).build()
        self.get_date = CommandHandler('time', get_date)
        self.start_handler = CommandHandler('start', start)
        # self.echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
        self.default_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), check_reply)
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
        repeating_interval = 60*5
        for pill_config in PILL_PROGRAMMING:
            time_value = pill_config[pill_time_key]
            log.info('date plan =' + str(time_value))
            self.job_queue.run_daily(send_message, data=[self.get_question(pill_list=pill_config[pill_list_key]),
                                                         pill_config[pill_list_key]],
                                     time=time_value, name="pill_reminder")
            for i in range(5):
                self.job_queue.run_daily(send_reminder, data=self.get_question(pill_list=pill_config[pill_list_key],
                                                                               is_reminder=True),
                                         time=time_value + timedelta(seconds=30*(1+i)), name="pill_reminder_"+str(1+i))

    def activate_handler(self):
        # activate all the handler
        self.application.add_handler(self.start_handler)
        # self.application.add_handler(self.echo_handler)
        self.application.add_handler(self.get_date)
        self.application.add_handler(self.default_handler)
        self.application.add_handler(self.unknown_handler)  # esto debe ser el ultimo handler
        self.application.run_polling()


if __name__ == '__main__':
    BotApplication()
