import requests
import os
from dotenv import load_dotenv

load_dotenv()
bot_token = os.getenv("TOKEN")
ngrok_url = os.getenv("WEBHOOK_URL")

url = f"https://api.telegram.org/bot{bot_token}/setWebhook?url={ngrok_url}/webhook"
print(requests.get(url).json())