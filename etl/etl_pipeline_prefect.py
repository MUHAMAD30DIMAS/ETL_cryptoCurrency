from prefect import flow, task
import requests
import pandas as pd
import pandas_gbq
from google.cloud import bigquery
from google.oauth2 import service_account

@task
def fetch_coingecko_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 20,
        'page': 1,
        'sparkline': False
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    df = pd.DataFrame(data)
    return df

@task
def clean_and_enrich_crypto_data(df):
    # Cleaning logic
    keep_cols = [
        'id', 'symbol', 'name', 'current_price', 'market_cap', 'total_volume',
        'price_change_percentage_24h', 'last_updated', 'ath'
    ]
    df = df[keep_cols]
    df.dropna(inplace=True)
    df['last_updated'] = pd.to_datetime(df['last_updated'])
    # Enrichment logic dari enrich_crypto_data
    df['ath_diff'] = df['ath'] - df['current_price']
    df['ath_gap_pct'] = ((df['ath'] - df['current_price']) / df['ath']) * 100
    df['vol_to_market_cap'] = df['total_volume'] / df['market_cap']
    df['cap_category'] = pd.cut(
        df['market_cap'],
        bins=[0, 1e9, 10e9, 1e13],
        labels=['Small Cap', 'Mid Cap', 'Large Cap']
    )
    df['change_direction'] = df['price_change_percentage_24h'].apply(
        lambda x: 'up' if x > 0 else ('down' if x < 0 else 'no change')
    )
    df['ath_status'] = df['ath_gap_pct'].apply(
        lambda x: 'near ATH' if x < 10 else ('far from ATH' if x > 30 else 'moderate')
    )
    return df

@task
def load_to_bigquery(df):
    table_id = "API_CRYPTO_DASHBOARD.crypto_boys"
    project_id = "api-crypto-dashboard"
    key_path = "../config/api-crypto-dashboard-4d7f7e155f6b.json"
    credentials = service_account.Credentials.from_service_account_file(
        key_path, scopes=["https://www.googleapis.com/auth/bigquery"]
    )
    pandas_gbq.to_gbq(
        df,
        destination_table=table_id,
        project_id=project_id,
        credentials=credentials,
        if_exists="replace" 
    )
    print(f"Data berhasil diupload ke BigQuery tabel: {table_id}")

@flow
def main():
    raw = fetch_coingecko_data()
    cleaned = clean_and_enrich_crypto_data(raw)
    load_to_bigquery(cleaned)
    print("ETL pipeline selesai!")

if __name__ == "__main__":
    main()

