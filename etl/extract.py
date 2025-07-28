
import requests
import pandas as pd
import logging
logging.basicConfig(level=logging.INFO)

def fetch_coingecko_data():

    """
    Fetches top 20 cryptocurrency data from CoinGecko API.

    Returns a pandas DataFrame containing the data.
    """

    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 20,      # Top 20 coin
        'page': 1,
        'sparkline': False
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    logging.info(f"Data fetched from {url}")
    df = pd.DataFrame(data)
    df.to_csv("../data/raw_crypto.csv", index=False)
    return df

if __name__ == "__main__":
    fetch_coingecko_data()
