import os
import time
import requests
import pandas as pd
from dotenv import load_dotenv
# from telegram import Bot

load_dotenv()

# Configurações do bot do Telegram
# TOKEN = os.getenv('TELEGRAM_TOKEN')
# CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
# bot = Bot(token=TOKEN)

def get_cripto_price():

    url = "https://api.coingecko.com/api/v3/coins/polkadot"
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

    try:
        response = requests.get(url)
        if response.status_code >= 200 or response.status_code <= 299:
            data = response.json()

            price = data['market_data']['current_price']['brl']
            return {
                'cripto': 'Polkadot',
                'price': price,
                'timestamp': timestamp
            }
        else:
            print('Ocorreu um erro ao conectar ao serviço do CoinMarketCap ao tentar acessar o preço do polkadot!')
            return None
    except Exception as exc:
        print(f'Erro: {exc}')
        raise

def convert_currency(value):
    return f'R$ {str(value).replace('.',',')}'


if __name__=='__main__':

    oldprice = get_cripto_price()['price']

    while True:
        data = get_cripto_price()
        
        price = data['price']

        if price < 0.9 * oldprice:
            print(f'!!!!!!!!!!!!!!!!!!\nO preço do Polkadot caiu 10%:\nPreço Anterior: {convert_currency(oldprice)}\nPreço Atual: {convert_currency(price)}\n!!!!!!!!!!!!!!!!!!')
            newprice = price
        elif price > 1.1 * oldprice:
            print(f'!!!!!!!!!!!!!!!!!!\nO preço do Polkadot subiu 10%:\nPreço Anterior: {convert_currency(oldprice)}\nPreço Atual: {convert_currency(price)}\n!!!!!!!!!!!!!!!!!!')
            newprice = price
        else:
            print(f"Preço atual do Polkadot: {convert_currency(price)}")
            
        time.sleep(10)