import time
import asyncio
from extract_price import get_cripto_price, convert_currency
from db_utils import create_connection, send_query, save_to_database
from bot_telegram import send_telegram_message

PERCENTAGE_ALERT = 0.05
COIN = "polkadot"
SEND_ALL = False
def create_message(oldprice, price, coin, price_status='atual', percentage_alert=10):
    match price_status:
        case 'atual':
            return f"Preço atual do {coin.capitalize()}: {convert_currency(price)}"
        case 'aumento':
            return f'!!!!!!!!!!!!!!!!!!\nO preço do {coin.capitalize()} subiu {percentage_alert*100} %:\nPreço Anterior: {convert_currency(oldprice)}\nPreço Atual: {convert_currency(price)}\n!!!!!!!!!!!!!!!!!!'
        case 'queda':
            return f'!!!!!!!!!!!!!!!!!!\nO preço do {coin.capitalize()} caiu {percentage_alert*100} %:\nPreço Anterior: {convert_currency(oldprice)}\nPreço Atual: {convert_currency(price)}\n!!!!!!!!!!!!!!!!!!'

async def main():    

    data = get_cripto_price(COIN)
    price = data['price']
    oldprice = data['price']

    while True:
        data = get_cripto_price(COIN)
        
        price = data['price']

        if price < (1-PERCENTAGE_ALERT) * oldprice:
            message = create_message(oldprice, price, coin=COIN, price_status='queda', percentage_alert=PERCENTAGE_ALERT)
            await send_telegram_message(message, send_all=SEND_ALL)

        elif price > (1+PERCENTAGE_ALERT) * oldprice:
            message = create_message(oldprice, price, coin=COIN, price_status='aumento', percentage_alert=PERCENTAGE_ALERT)
            await send_telegram_message(message, send_all=SEND_ALL)

        else:
            message = create_message(oldprice, price, coin=COIN, price_status='atual')
            await send_telegram_message(message, send_all=SEND_ALL)
            
        await asyncio.sleep(600)


asyncio.run(main())