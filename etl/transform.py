import pandas as pd

def enrich_crypto_data(df):
    
    """
    Enriches the given DataFrame with additional columns:

    1. `ath_diff`: difference between ATH and current price
    2. `ath_gap_pct`: percentage gap between ATH and current price
    3. `vol_to_market_cap`: ratio of total volume to market capitalization
    4. `cap_category`: categorization of market capitalization into Small, Mid, or Large Cap
    5. `change_direction`: direction of price change in the last 24 hours (up, down, or no change)
    6. `ath_status`: status of being near or far from ATH (near ATH, far from ATH, or moderate)

    Returns the enriched DataFrame.
    """
    # 1. Difference between ATH and current price
    df['ath_diff'] = df['ath'] - df['current_price']
    # 2. Gap percentage to ATH(All Time High)
    df['ath_gap_pct'] = ((df['ath'] - df['current_price']) / df['ath']) * 100
    # 3. Ratio of total volume to market capitalization
    df['vol_to_market_cap'] = df['total_volume'] / df['market_cap']
    # 4. Market capitalization category
    df['cap_category'] = pd.cut(
        df['market_cap'],
        bins=[0, 1e9, 10e9, 1e13],
        labels=['Small Cap', 'Mid Cap', 'Large Cap']
    )
    # 5. Price change direction
    df['change_direction'] = df['price_change_percentage_24h'].apply(
        lambda x: 'up' if x > 0 else ('down' if x < 0 else 'no change')
    )
    # 6. ATH status (near ATH, far from ATH, or moderate)
    df['ath_status'] = df['ath_gap_pct'].apply(
        lambda x: 'near ATH' if x < 10 else ('far from ATH' if x > 30 else 'moderate')
    )
    return df

def clean_and_enrich_crypto_data(input_csv="../data/raw_crypto.csv", output_csv="../data/clean_crypto.csv"):
    """
    Cleans and enriches cryptocurrency data from a CSV file.

    This function reads cryptocurrency data from the specified input CSV file,
    retains relevant columns, drops rows with missing values, converts the
    'last_updated' column to datetime format, and enriches the data with
    additional calculated columns. The enriched data is then saved to the
    specified output CSV file.

    Parameters:
    - input_csv (str): Path to the input CSV file containing raw cryptocurrency data.
    - output_csv (str): Path to the output CSV file where cleaned and enriched data will be saved.

    Returns:
    - pd.DataFrame: The cleaned and enriched DataFrame.
    """

    df = pd.read_csv(input_csv)
    keep_cols = [
        'id', 'symbol', 'name', 'current_price', 'market_cap', 'total_volume',
        'price_change_percentage_24h', 'last_updated', 'ath'
    ]
    df = df[keep_cols]
    df.dropna(inplace=True)
    df['last_updated'] = pd.to_datetime(df['last_updated'])
    df = enrich_crypto_data(df)
    df.to_csv(output_csv, index=False)
    return df

if __name__ == "__main__":
    clean_and_enrich_crypto_data()
