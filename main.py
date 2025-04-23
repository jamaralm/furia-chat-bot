import requests
from env.settings import TOKEN, CHAT_ID

MESSAGE = "Fala, Pantera! 🐾 O bot da FURIA está online!"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": MESSAGE
}

response = requests.post(url, data=payload)

print("Status code:", response.status_code)
try:
    print("Resposta do Telegram:", response.json())
except Exception as e:
    print("Erro ao tentar decodificar JSON:", e)
    print("Texto da resposta:", response.text)