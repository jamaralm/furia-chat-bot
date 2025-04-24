from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import Application
from app.bot import create_bot

app = FastAPI()
bot_app: Application = None  # variável global

@app.on_event("startup")
async def startup():
    global bot_app
    bot_app = await create_bot()
    print("Bot iniciado e webhook configurado.")

@app.post("/webhook")
async def telegram_webhook(req: Request):
    data = await req.json()
    update = Update.de_json(data, bot_app.bot)
    await bot_app.process_update(update)
    return {"ok": True}