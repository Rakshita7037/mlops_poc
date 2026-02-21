import sqlite3
import pandas as pd
import requests
from datetime import datetime

def ingest_sql():
    conn = sqlite3.connect("data/churn.db")
    df_sql = pd.read_sql("SELECT * FROM customers", conn)
    conn.close()
    print("SQL rows:", len(df_sql))
    return df_sql

# def ingest_api():
#     url = "http://localhost:9100/new_customers"
#     response = requests.get(url)
#     df_api = pd.DataFrame(response.json())
#     print("API rows:", len(df_api))
#     return df_api

if __name__ == "__main__":

    df_sql = ingest_sql()
    # df_api = ingest_api()

    # Merge both sources
    # df_combined = pd.concat([df_sql, df_api], ignore_index=True)
    df_combined = df_sql.copy()

    # Remove duplicates
    df_combined = df_combined.drop_duplicates(subset=["customer_id"])

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"data/raw/telecom_raw_{timestamp}.csv"

    df_combined.to_csv(path, index=False)

    print("Unified dataset saved at:", path)
