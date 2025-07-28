from extract import fetch_coingecko_data
from transform import clean_and_enrich_crypto_data
from load import load_to_bigquery
import pandas as pd

import sys
import os

sys.path.append('./etl')

def main():

    """
    Runs the entire ETL pipeline from extracting data from CoinGecko to
    loading the enriched data into BigQuery.

    1. Extracts data from CoinGecko API and saves it as a CSV file in
       the `../data/raw_crypto.csv` file.
    2. Cleans and enriches the raw data by dropping irrelevant columns,
       handling missing values, and adding additional columns like
       `ath_diff`, `ath_gap_pct`, `vol_to_market_cap`, `cap_category`,
       `change_direction`, and `ath_status`.
    3. Loads the enriched data into BigQuery as a table named
       `API_CRYPTO_DASHBOARD.crypto_boys`.

    Does not return anything.

    """
    # 1. Extract data dari CoinGecko
    fetch_coingecko_data() 

    # 2. Transform + Enrich data
    df = clean_and_enrich_crypto_data()  

    # 3. Load to BigQuery
    load_to_bigquery(df)  

    print("ETL selesai. Data terupdate di BigQuery!")

if __name__ == "__main__":
    main()
