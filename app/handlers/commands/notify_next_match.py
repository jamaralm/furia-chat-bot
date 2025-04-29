from telegram import Update, Bot
from telegram.ext import ContextTypes, CallbackQueryHandler
from pathlib import Path
from .proximapartida import check_match_date
import os, json, asyncio

NOTIFY_USERS_FILE = Path("app/data/notify_users.json")
TOKEN = os.getenv("TOKEN")
bot = Bot(TOKEN)

async def notify_next_match_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()

    if NOTIFY_USERS_FILE.exists():
        with open(NOTIFY_USERS_FILE, 'r') as file:
            users = json.load(file)
    else:
         return []
    
    if not user_id in users:
        users.append(user_id)
        with open(NOTIFY_USERS_FILE, 'w') as file:
            json.dump(users, file)

    await query.edit_message_text(text="🔔 Você será notificado antes da próxima partida!")
        
async def start_notify_loop():
    while True:
        await asyncio.sleep(60)

        time_remaining, next_match = check_match_date()

        if time_remaining is None or next_match is None:
            continue
        
        if time_remaining.total_seconds() <= 1800:
            if NOTIFY_USERS_FILE.exists():
                with open(NOTIFY_USERS_FILE, 'r') as file:
                    users = json.load(file)

            for user_id in users:
                try:
                    await bot.send_message(
                        chat_id=user_id,
                        text=(
                                f"🚨 Está chegando a hora!\n"
                                f"🔥 FURIA vs {next_match['opponent']}\n"
                                f"🏆 {next_match['tournament']}\n"
                                f"📅 Hoje às {next_match['time']}!"
                            )
                    )
                except Exception as e:
                    print(f"ERROR: {e}")
            
            with open(NOTIFY_USERS_FILE, 'w') as file:
                json.dump([], file)

def get_handler():
    return CallbackQueryHandler(notify_next_match_callback, pattern="^notify_next_match$")