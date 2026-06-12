import requests
import psycopg2

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "ids": "bitcoin,ethereum,solana"
}

data = requests.get(url, params=params).json()

conn = psycopg2.connect(
    host="postgres",
    port=5432,
    database="airflow_db",
    user="airflow",
    password="airflow"
)

cur = conn.cursor()

for coin in data:

    cur.execute(
        """
        INSERT INTO crypto_prices
        (
            coin_name,
            price_usd,
            market_cap,
            captured_at
        )
        VALUES (%s,%s,%s,%s)
        """,
        (
            coin["name"],
            coin["current_price"],
            coin["market_cap"],
            coin["last_updated"]
        )
    )

conn.commit()

cur.close()
conn.close()

print("Loaded crypto data")
