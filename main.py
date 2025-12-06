import requests as r
from bs4 import BeautifulSoup


def get_price_information(ticker, exchange):

    url = f"https://www.google.com/finance/qoute/{ticker}:{exchange}"
    resp = r.get(url) 
    soup =BeautifulSoup(resp.content, "html.parser")

    price_div = soup.find("div",attrs={"data_last_price": true})
    #  price = float(price_div {"data-last-price"})
   
    return {
        "ticker" : ticker,
        "exchange": exchange,
        "price":price,
        "currency":currency
    }
print("hey")
if __name__ == "__main__":
    print("hello")
    print(get_price_information("MSFT", "NASDAQ"))
    print("hi")    