from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from app.handle_data import load_data

MESSAGES_URL = "app/data/messages.json"

error_message = load_data(MESSAGES_URL)
error_message = error_message['error']

async def start(update:Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        start_message = load_data(MESSAGES_URL)
        start_message = start_message['start']

        await update.message.reply_text(start_message)
    except:
        await update.message.reply_text(error_message)

def get_handler():
    return CommandHandler("start", start)