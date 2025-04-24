from telegram.ext import ApplicationBuilder, CommandHandler
from app.handlers.handlers_commands import start, help, next_match, previows_match
from dotenv import load_dotenv
import os

load_dotenv()

async def create_bot():
    bot_token = os.getenv("TOKEN")
    ngrok_url = os.getenv("NGROK_URL")

    app = ApplicationBuilder().token(bot_token).build()

    #Registro de Comandos
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("nextmatch", next_match))
    app.add_handler(CommandHandler("previowsmatch", previows_match)) 

    await app.initialize()
    await app.bot.set_webhook(f"{ngrok_url}/webhook")
    return app