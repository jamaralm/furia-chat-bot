from telegram.ext import ApplicationBuilder, CommandHandler
from app.handlers.start import start
from dotenv import load_dotenv
import os

load_dotenv()

async def create_bot():
    bot_token = os.getenv("TOKEN")
    ngrok_url = os.getenv("NGROK_URL")

    app = ApplicationBuilder().token(bot_token).build()
    app.add_handler(CommandHandler("start", start))

    await app.initialize()
    await app.bot.set_webhook(f"{ngrok_url}/webhook")
    return app