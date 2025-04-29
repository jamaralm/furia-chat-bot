from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes, CommandHandler
from app.handle_data import load_data
from app.handle_data import load_data

PLAYERS_URL = "app/data/players.json"

async def players(update:Update, context:ContextTypes.DEFAULT_TYPE):
    players = load_data(PLAYERS_URL)

    keyboard = [
        [InlineKeyboardButton(player['name'], callback_data=f"player_{player['id']}")]
        for player in players
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🎮 Jogadores da FURIA:\nSelecione um jogador para ver estatísticas:",
        reply_markup=reply_markup
    )

def get_handler():
    return CommandHandler("jogadores", players)