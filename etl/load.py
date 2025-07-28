import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
import pandas_gbq

def load_to_bigquery(
    df, 
    table_id="API_CRYPTO_DASHBOARD.crypto_boys", 
    project_id="api-crypto-dashboard", 
    key_path="../config/api-crypto-dashboard-4d7f7e155f6b.json"
):
    
    """
    Uploads a Pandas DataFrame to BigQuery.

    Parameters:
    - df (pd.DataFrame): The DataFrame to be uploaded.
    - table_id (str): The destination table ID in the format "dataset_id.table_id". Default: "API_CRYPTO_DASHBOARD.crypto_boys"
    - project_id (str): The GCP project ID. Default: "api-crypto-dashboard"
    - key_path (str): The path to the service account key file. Default: "../config/api-crypto-dashboard-4d7f7e155f6b.json"

    Returns:
    - None
    """
    
    # Setup credentials
    credentials = service_account.Credentials.from_service_account_file(
        key_path, scopes=["https://www.googleapis.com/auth/bigquery"]
    )
    # Upload ke BigQuery
    pandas_gbq.to_gbq(
        df,
        destination_table=table_id,
        project_id=project_id,
        credentials=credentials,
        if_exists="replace" 
    )
    print(f"Data berhasil diupload ke BigQuery tabel: {table_id}")
