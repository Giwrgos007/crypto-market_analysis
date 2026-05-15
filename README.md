# Crypto Market Data Pipeline & Analytics

A modern, object-oriented end-to-end data engineering and analytics project. The application automates the process of fetching live cryptocurrency data via a REST API, storing it inside a structured relational database, and generating executive-ready market insights.

## 🚀 Features
- **Automated Data Ingestion:** Connects to the CoinGecko API to fetch real-time market data, parses the JSON payload, cleans it, and exports it into a structured CSV file using `Pandas`.
- **Relational Database Storage:** Automatically creates schemas and maps data types inside a local `PostgreSQL` instance for robust storage.
- **Analytical SQL Querying:** Utilizes advanced SQL scripting (Aggregations, Ordering, and Filtering) to extract business-critical metrics from the database.
- **Object-Oriented Visualization:** Implements modular Python classes built with `Matplotlib` and `Seaborn` to dynamically extract database views and convert them into presentation-ready visuals.

## 📂 File Structure
- `main.py`: The central execution file that handles database connectivity, populates local data structures, and orchestrates the analytical visualizations.
- `generate_charts.py`: The core pipeline script managing the live API connection, data cleaning, and local storage formats.
- `market_plots.py`: Contains the `MarketVisualizer` class for market cap rankings.
- `price_plots.py`: Contains the `PriceVisualizer` class for analyzing token prices.
- `trend_plots.py`: Contains the `TrendVisualizer` class for short-term price momentum.
- `crypto_data.csv`: The cleaned, tabular dataset extracted from the API, serving as the source-of-truth file.

---

## 📊 Data Exploration & Insights (SQL Queries)

### 1. Database Table Verification
*Validating the table schema and ensuring all 100 coin profiles were accurately mapped into the PostgreSQL instance:*
```sql
SELECT * FROM crypto_prices 
LIMIT 10;
