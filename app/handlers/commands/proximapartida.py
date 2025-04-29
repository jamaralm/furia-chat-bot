from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler
from app.handle_data import check_match_date


MATCHES_URL = "app/data/matches.json"

async def match(update:Update, context: ContextTypes.DEFAULT_TYPE):
    time_remaining, match = check_match_date()

    if not match:
        await update.message.reply_text("🚫 Nenhuma partida futura encontrada!")
        return
    
    days = time_remaining.days
    hours, remainder = divmod(time_remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    time_remaining_formatted = f"{days} Dias {hours} Horas {minutes} Minutos"

    next_matches = (
    f"🔥 FURIA vs {match['opponent']} 🔥\n"
    f"🏆 Torneio: {match['tournament']}\n"
    f"📅 Data: {match['date']} às {match['time']}\n"
    f"⭐ Possível MVP: {match['expected_highlight'].upper()}\n"
    f"📝 {match['notes']}\n"
    f"Tempo restante: {time_remaining_formatted}"
    )

    keyboard = [
        [InlineKeyboardButton("🔔 Notificar próximo jogo", callback_data="notify_next_match")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        f"🔥 Proxima Partida:\n{next_matches}",
        reply_markup=reply_markup    
    )

def get_handler():
    return CommandHandler('proximapartida', match)