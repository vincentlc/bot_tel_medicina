from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ContextTypes
from text import reply_invalid_command, reception_of_message_deactivated
from datetime import datetime
from config import CHAT_ID
from message_handler import check_message_ok, ReaderActivation
import logging

log = logging.getLogger(__name__)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

reader = ReaderActivation()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Soy un bot, puede hablarme!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


async def get_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=reply_invalid_command)


async def send_message(context: ContextTypes.DEFAULT_TYPE):
    reader.toggle_wait_reply(True)
    await context.bot.send_message(chat_id=CHAT_ID, text=context.job.data)


async def check_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    """Read the message and do the according action"""
    user = update.message.from_user.first_name
    message_received = update.message.text
    log.info("message of %s: %s", user, message_received)

    if reader.get_if_waiting_rely():  # if currently waiting for an answer
        reply_text, status = check_message_ok(message_received)  # check if the message received is valid
        if status:
            reader.toggle_wait_reply(False)     # deactivate the reader
            await context.bot.send_message(chat_id=update.effective_chat.id, text=reception_of_message_deactivated)
        await update.message.reply_text(
            reply_text,
            reply_markup=ReplyKeyboardRemove(),
        )
