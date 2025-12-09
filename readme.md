# Google Finance Price Scraper

This project contains a Python script that scrapes and extracts stock price information from Google Finance using a given ticker symbol and exchange. The data is then returned in a structured format, making it easy to access and use for further analysis or integration into other systems.

## Features

- Scrape real-time stock price information from Google Finance.
- Extract the ticker symbol, exchange, price, and currency of a given stock.
- Simple function-based implementation for easy integration into other projects.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

You can install the required dependencies using `pip`:

```bash
pip install requests beautifulsoup4

# How It Works

The main function get_price_information(ticker, exchange) scrapes Google Finance for the stock data corresponding to the provided ticker symbol and exchange.

## Function Breakdown:

- URL Construction: A URL is created dynamically based on the ticker symbol and exchange (e.g., https://www.google.com/finance/quote/{ticker}:{exchange}).
- HTTP Request: The requests library sends a GET request to retrieve the HTML content of the page.
- HTML Parsing: The BeautifulSoup library is used to parse the HTML and extract the relevant information, specifically the last traded price and currency.
- Data Extraction: The price and currency are extracted from the HTML div element with the data-last-price and data-currency-code attributes.
- Return Data: A dictionary is returned with the following keys: ticker, exchange, price, and currency.

## example output :
```json
{
    "ticker": "GOOGL",
    "exchange": "NASDAQ",
    "price": 2781.44,
    "currency": "USD"
}

# Notes

- Rate Limiting: Be mindful of making too many requests in a short period, as Google might block or rate-limit requests.
- Accuracy: The accuracy of the data depends on the structure of the Google Finance page, which might change over time.
- Error Handling: The current implementation does not have error handling for cases where the page is not available or the structure changes. You may want to add checks or try-except blocks in a production environment.
