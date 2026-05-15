import matplotlib.pyplot as plt
import seaborn as sns


class PriceVisualizer:

    def __init__(self, dataframe):
        self.df = dataframe.sort_values(by="market_cap", ascending=False).head(
            10
        )

    def generate_chart(self):
        plt.figure(figsize=(10, 6))
        sns.barplot(
            data=self.df,
            x="current_price",
            y="symbol",
            palette="viridis",
            hue="symbol",
        )
        plt.title("Price Comparison of Top 10 Cryptocurrencies")
        plt.xlabel("Current Price (USD)")
        plt.ylabel("Coin Symbol")
        plt.xscale("log")
        plt.tight_layout()
        plt.savefig("price_comparison.png")
        plt.show()