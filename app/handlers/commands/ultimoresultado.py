from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from app.handle_data import load_data

PREVIOWS_MATCHES_URL = "app/data/previows_matches.json"

async def previows_match(update:Update, context:ContextTypes.DEFAULT_TYPE):
    previows_matches = load_data(PREVIOWS_MATCHES_URL)
    previows_matches = previows_matches[:1]

    match = previows_matches[0]

    # Formata os mapas corretamente
    formatted_maps = "\n".join(
        [f"{map_name} - {score.replace('-', ' X ')}" for map_name, score in match['maps'].items()]
    )

    # Mensagem final com todas as informações
    result = (
        f"{match['result']} - {match['date']}\n"
        f"🏆 Campeonato: {match['tournament']}\n"
        f"🗺️ Mapas:\n{formatted_maps}\n"
        f"🌟 Destaque: {match['highlight']}\n"
        f"📝 Observações: {match['notes']}"
    )

    await update.message.reply_text(f"🔥 Partida Anterior:\n🎮{result}")

def get_handler():
    return CommandHandler('ultimoresultado', previows_match)