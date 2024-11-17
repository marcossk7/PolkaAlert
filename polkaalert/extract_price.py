import time
import requests

def get_cripto_price(coin):

    url = f"https://api.coingecko.com/api/v3/coins/{coin}"
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

    try:
        response = requests.get(url)
        if response.status_code >= 200 or response.status_code <= 299:
            data = response.json()

            price = data['market_data']['current_price']['brl']
            return {
                'cripto': f'{coin}'.capitalize(),
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