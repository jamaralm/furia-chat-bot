from telegram import Update
from telegram.ext import ContextTypes
from app.messages import start_message, help_message
from app.data import next_matches, previows_matches

async def start(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(start_message)

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(help_message)

async def next_match(update:Update, context: ContextTypes.DEFAULT_TYPE):
    matches = "\n".join(f"{match['teams']} - {match['data']}" for match in next_matches)
    await update.message.reply_text(f"Proximos Jogos:\n{matches}")

async def previows_match(update:Update, context:ContextTypes.DEFAULT_TYPE):
    result = "\n".join(f"{match['result']} - {match['data']}" for match in previows_matches)
    await update.message.reply_text(f"Jogos Anteriores:\n{result}")