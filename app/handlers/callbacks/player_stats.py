from telegram import Update
from telegram.ext import ContextTypes, CallbackQueryHandler
from app.handle_data import load_data

PLAYERS_URL = "app/data/players.json"

async def player_stats_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    player_id = query.data.split('_')[1]
    players = load_data(PLAYERS_URL)

    player = next((p for p in players if p['id'] == player_id), None)

    if not player:
        await query.edit_message_text("❌ Jogador não encontrado.")
        return 
    
    stats_text = (
        f"📊 Estatísticas de {player['name']}:\n"
        f"🔫 Função: {player['role']}\n"
        f"📈 Rating: {player['statistcs']['Rating']}\n"
        f"💀 K/D: {player['statistcs']['KDA']}\n"
        f"🔥 HS%: {player['statistcs']['HS%']}"
    )

    await query.edit_message_text(stats_text)

def get_handler():
    return CallbackQueryHandler(player_stats_callback, pattern="^player_")
    