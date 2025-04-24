from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from app.handle_data import load_data

MATCHES_URL = "app/data/matches.json"

async def next_match(update:Update, context: ContextTypes.DEFAULT_TYPE):
    matches = load_data(MATCHES_URL)
    matches = matches[:1]
    next_matches = "\n🎮".join([f"FURIA X {match['opponent']} \n{match['date']} as {match['time']} \nCampeonato: {match['tournament']}" for match in matches])
    
    await update.message.reply_text(f"🔥 Proxima Partida:\n{next_matches}")

def get_handler():
    return CommandHandler('proximapartida', next_match)