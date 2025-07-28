#  Crypto ETL Pipeline (Manual Version)

This project is an ETL (Extract, Transform, Load) pipeline for retrieving cryptocurrency market data from the [CoinGecko API](https://www.coingecko.com/en/api), enriching and cleaning the dataset, and uploading it to Google BigQuery.

> ⚠️ **Note:** The ETL workflow is structured for [Prefect](https://docs.prefect.io/), but Prefect orchestration is **not yet active**. The pipeline can currently be run manually step-by-step.

---

## 📁 Project Structure
PortProject_API/
etl/
  ├── extract.py                    # Extracts data from CoinGecko API
  ├── transform.py                  # Cleans & enriches the data
  ├── load.py                       # Uploads data to BigQuery
  ├── main.py                       # Runs the ETL pipeline (manual)
  ├── etl_pipeline_prefect.py       # Prefect pipeline (not yet active)
├── config/
  │   └── api-crypto-dashboard-xxx.json   # GCP credentials (keep private)
├── data/
  │   ├── raw_crypto.csv            # Raw data (output, ignored)
  │   └── clean_crypto.csv          # Cleaned/enriched data (output, ignored)
├── requirements.txt
├── .gitignore
└── README.md


---

## ⚙️ How to Run (Manual Mode)

### 1. Install Dependencies

```bash
  pip install -r requirements.txt

**2. Run Each Step**
Extract:
```bash 
  python extract.py

Transform:
```bash
  python transform.py

Load:
```python
  from load import load_to_bigquery
  import pandas as pd

  df = pd.read_csv("data/clean_crypto.csv")
  load_to_bigquery(df)


🧪 Prefect Pipeline (Not Yet Active)
The file etl_pipeline_prefect.py is set up for Prefect orchestration, but Prefect is not yet configured and tested in this repo.
Once Prefect is configured, you can run the entire ETL flow with:
```bash
  python etl_pipeline_prefect.py

📝 Notes
- Store your GCP service account key in: config/api-crypto-dashboard-xxx.json

- This file is already excluded in .gitignore

- Make sure your BigQuery project and tables are set up and accessible

- Do not share your credentials publicly


✅ Deployment Checklist:

 - Manual pipeline works (extract, transform, load) ✅

 - Prefect CLI & agent installed

 - Prefect pipeline tested end-to-end

 - Automated scheduling via Prefect Cloud or local agent

📦 Requirements
List in requirements.txt:
```nginx
  pandas
  requests
  pandas-gbq
  google-cloud-bigquery
  google-auth
  prefect

👨‍💻 Author
Made with ❤️ by [Muhamad Dimas Wijaya Kesuma]
