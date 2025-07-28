# 🚀 PortProject_API – Crypto ETL Pipeline (Manual Version)

This project is an ETL (Extract, Transform, Load) pipeline for retrieving cryptocurrency market data from [CoinGecko API](https://www.coingecko.com/en/api), enriching and cleaning the dataset, and uploading it to Google BigQuery.

> ⚠️ **Note:** Prefect orchestration is included but **not yet active**. Run the pipeline manually using `main.py`.

---

## 📁 Project Structure

```text
PortProject_API/
├── etl/
|   ├── extract.py # Extracts data from CoinGecko API
|   └── transform.py # Cleans & enriches the data
|   └── load.py # Uploads data to BigQuery
|   └── main.py
|   └── etl_pipeline_prefect.py # Prefect pipeline (not yet active)
├── config/
│   └── api-crypto-dashboard-xxx.json # GCP credentials (keep private)
├── data/
│   ├── raw_crypto.csv
│   └── clean_crypto.csv
├── requirements.txt
├── .gitignore
└── README.md
```

### ⚙️ How to Run (Manual Mode)
Install dependencies:
```bash
pip install -r requirements.txt
```
Run ETL pipeline:
```bash
python main.py
```
#### 📝 Notes
  1. Store your GCP service account key in:
  ```config/api-crypto-dashboard-xxx.json```

  2. Data output files are stored in /data (ignored by git).

  3. Do not share your credentials publicly.

#### ✅ Deployment Checklist
   ✅Manual pipeline works (main.py)

   Prefect orchestration tested & activated

   Automated scheduling via Prefect

#### 📦 Requirements
List in requirements.txt:
```nginx
pandas
requests
pandas-gbq
google-cloud-bigquery
google-auth
prefect
```
Install with:
```bash
pip install -r requirements.txt
```

👨‍💻 Author
Made with ❤️ by [Muhamad Dimas Wijaya Kesuma]
