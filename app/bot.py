from telegram.ext import ApplicationBuilder, Updater
from app.handlers import handlers_commands
from dotenv import load_dotenv
import os

load_dotenv()

async def create_bot():
    bot_token = os.getenv("TOKEN")
    ngrok_url = os.getenv("NGROK_URL")

    app = ApplicationBuilder().token(bot_token).build()

    handlers_commands.register_handlers(app)

    await app.initialize()
    await app.bot.set_webhook(f"{ngrok_url}/webhook")
    return app