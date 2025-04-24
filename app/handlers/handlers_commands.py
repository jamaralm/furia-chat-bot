from telegram import Update
from telegram.ext import ContextTypes
from app.handle_data import load_data

MATCHES_URL = "app/data/matches.json"
MESSAGES_URL = "app/data/messages.json"
PLAYERS_URL = "app/data/players.json"
PREVIOWS_MATCHES_URL = "app/data/previows_matches.json"

error_message = load_data(MESSAGES_URL)
error_message = error_message['error']

async def start(update:Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        start_message = load_data(MESSAGES_URL)
        start_message = start_message['start']

        await update.message.reply_text(start_message)
    except:
        await update.message.reply_text(error_message)

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_message = load_data(MESSAGES_URL)
    help_message = help_message['help']

    await update.message.reply_text(help_message)

async def next_match(update:Update, context: ContextTypes.DEFAULT_TYPE):
    matches = load_data(MATCHES_URL)
    matches = matches[:5]
    next_matches = "\n🎮".join([f"{match['teams']} - {match['data']}" for match in matches])
    
    await update.message.reply_text(f"🔥 Proximos Jogos:\n🎮{next_matches}")

async def previows_match(update:Update, context:ContextTypes.DEFAULT_TYPE):
    previows_matches = load_data(PREVIOWS_MATCHES_URL)
    previows_matches = previows_matches[:5]
    result = "\n🎮".join(f"{match['result']} - {match['data']}" for match in previows_matches)

    await update.message.reply_text(f"🔥 Jogos Anteriores:\n🎮{result}")

async def players(update:Update, context:ContextTypes.DEFAULT_TYPE):
    player_list = load_data(PLAYERS_URL)

    players = "\n\n".join(f"{player['name']} - {player['role']}\n KDA: {player['statistcs']['KDA']}\n HS%: {player['statistcs']['HS%']}\n Rating: {player['statistcs']['Rating']}" for player in player_list)

    await update.message.reply_text(f"Nossos Jogadores:\n{players}")