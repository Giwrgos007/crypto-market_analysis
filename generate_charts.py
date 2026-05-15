import pandas as pd
import psycopg2

from market_plots import MarketVisualizer
from price_plots import PriceVisualizer
from trend_plots import TrendVisualizer

conn = psycopg2.connect(
    dbname="crypto_market",
    user="postgres",
    password="123456789",
    host="localhost",
    port="5432",
)

query = "SELECT id, symbol, current_price, market_cap, price_change_percentage_24h, total_volume FROM crypto_prices;"
df = pd.read_sql_query(query, conn)
conn.close()


print("Generating charts...")

price_chart = PriceVisualizer(df)
price_chart.generate_chart()

market_chart = MarketVisualizer(df)
market_chart.generate_chart()

trend_chart = TrendVisualizer(df)
trend_chart.generate_chart()

print("All charts have been generated and saved successfully!")