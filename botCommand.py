from telegram import Update, ReplyKeyboardRemove  # ,ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from text import reply_invalid_command, get_pill_remaining, get_extra_string_time
from datetime import datetime
from config import CHAT_ID
from message_handler import check_message_ok, ReaderActivation
from pillHandler import PillChecker
from text import alert_message
import logging

log = logging.getLogger(__name__)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

reader = ReaderActivation()
pill_checker = PillChecker()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Soy un bot, puede hablarme!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


async def get_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=reply_invalid_command)


async def get_pill(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=get_pill_remaining(pill_checker.get_pill_list()))


async def send_message(context: ContextTypes.DEFAULT_TYPE):
    reader.toggle_wait_reply(True)
    pill_list, bot = context.job.data
    text_data = bot.get_question(pill_list=pill_list)
    pill_checker.update_last_pill_list(pill_list)  # update the last pill list to decrease
    await context.bot.send_message(chat_id=CHAT_ID, text=text_data)


async def send_reminder(context: ContextTypes.DEFAULT_TYPE):
    if reader.get_if_waiting_rely():
        pill_list, bot = context.job.data
        text_data = bot.get_question(pill_list=pill_list, is_reminder=True)
        pill_checker.update_last_pill_list(pill_list)  # update the last pill list to decrease
        await context.bot.send_message(chat_id=CHAT_ID, text=text_data)


async def send_alert(context: ContextTypes.DEFAULT_TYPE):
    status, value = pill_checker.is_alert_level()
    if status:
        await context.bot.send_message(chat_id=CHAT_ID, text=alert_message(value))


async def check_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    """Read the message and do the according action"""
    user = update.message.from_user.first_name
    message_received = update.message.text
    log.info("message of %s: %s", user, message_received)

    if reader.get_if_waiting_rely():  # if currently waiting for an answer
        reply_text, status = check_message_ok(message_received)  # check if the message received is valid
        if status:
            pill_checker.decrease_quantity(pill_checker.get_last_pill_list())
            reader.toggle_wait_reply(False)     # deactivate the reader
            # await context.bot.send_message(chat_id=update.effective_chat.id, text=reception_of_message_deactivated)
            # print(pill_checker.is_alert_level())
            await send_alert(context)
        await update.message.reply_text(
            reply_text,
            reply_markup=ReplyKeyboardRemove(),
        )

    return ''
