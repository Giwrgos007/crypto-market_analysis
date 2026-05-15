import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin&names=Bitcoin&symbols=btc&category=layer-1&price_change_percentage=1h"

response = requests.get(url)
data = response.json()

df_all = pd.DataFrame(data)

crypto_prices = [
    "id",
    "symbol",
    "current_price",
    "market_cap",
    "total_volume",
    "price_change_percentage_24h",
]
df = df_all[crypto_prices]

print(df)

df.to_csv("crypto_data.csv", index=False, encoding="utf-8")


