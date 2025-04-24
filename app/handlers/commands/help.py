from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from app.handle_data import load_data

MESSAGES_URL = "app/data/messages.json"

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_message = load_data(MESSAGES_URL)
    help_message = help_message['help']

    await update.message.reply_text(help_message)

def get_handler():
    return CommandHandler("help", help)