import os
import requests
import pandas as pd
from dotenv import load_dotenv
from telegram import Bot
import asyncio

load_dotenv()

# Configurações do bot do Telegram
TOKEN = os.getenv('TELEGRAM_TOKEN')
MEU_ID = os.getenv('TELEGRAM_MEU_ID')
URL = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

bot = Bot(token=TOKEN)

def get_ids(url):
    """Obtém os IDs dos usuários a partir do Telegram."""
    
    response = requests.get(url)
    data = response.json()
    return set(pd.json_normalize(data['result'])['message.from.id'].dropna().astype(int))

async def send_telegram_message(text:str, send_all:bool=False):
    """Envia uma mensagem para o Telegram."""

    ids = get_ids(URL)
    if send_all:
        for user_id in ids:
            await bot.send_message(chat_id=user_id, text=text)
    else:
        await bot.send_message(chat_id=MEU_ID, text=text)
        
if __name__ == '__main__':

    async def main():
        text = "Mensagem de Teste"
        await send_telegram_message(text)
    asyncio.run(main())
