import requests
from bs4 import BeautifulSoup
import json

def getData(symbol):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    url = f'https://finance.yahoo.com/quote/{symbol}'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    # Attempt to find the element
    stock_div = soup.find('div', {'class': 'D(ib) Mend(20px)'})

    # Check if the element is found
    if stock_div:
        try:
            price = stock_div.find_all('span')[0].text
            change = stock_div.find_all('span')[1].text
        except IndexError as e:
            print(f"Error retrieving data for {symbol}: {e}")
            return None
    else:
        print(f"Error retrieving data for {symbol}: Element not found")
        return None

    stock = {
        'symbol': symbol,
        'price': price,
        'change': change,
    }
    return stock

# Example usage
stock_symbols = ['AAPL', 'GOOGL', 'DOGE']
stockdata = []

for item in stock_symbols:
    result = getData(item)
    if result:
        stockdata.append(result)

print(stockdata)

with open('stockdata.json', 'w') as f:
 json.dump(stockdata, f)

print('Fin.')