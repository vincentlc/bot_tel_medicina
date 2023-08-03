from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ContextTypes
from text import reply_invalid_command
from datetime import datetime
from config import CHAT_ID
#from newBot import logging


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Soy un bot, puede hablarme!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


async def get_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=reply_invalid_command)


async def send_message(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=CHAT_ID, text=context.job.data)
    #await check_reply()


async def check_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    """Stores the selected gender and asks for a photo."""
    user = update.message.from_user
    #logging.info("Gender of %s: %s", user.first_name, update.message.text)
    await update.message.reply_text(
        "I see! Please send me a photo of yourself, "
        "so I know what you look like, or send /skip if you don't want to.",
        reply_markup=ReplyKeyboardRemove(),
    )

    return 'test'