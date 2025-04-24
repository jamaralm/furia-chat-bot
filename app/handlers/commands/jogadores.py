from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from app.handle_data import load_data

PLAYERS_URL = "app/data/players.json"

async def players(update:Update, context:ContextTypes.DEFAULT_TYPE):
    player_list = load_data(PLAYERS_URL)    

    players = "\n\n".join(f"{player['name']} - {player['role']}\n KDA: {player['statistcs']['KDA']}\n HS%: {player['statistcs']['HS%']}\n Rating: {player['statistcs']['Rating']}" for player in player_list)

    await update.message.reply_text(f"Nossos Jogadores:\n{players}")

def get_handler():
    return CommandHandler("jogadores", players)