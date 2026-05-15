import matplotlib.pyplot as plt
import seaborn as sns


class MarketVisualizer:

    def __init__(self, dataframe):
        self.df = dataframe.sort_values(by="market_cap", ascending=False).head(
            10
        )

    def generate_chart(self):
        plt.figure(figsize=(10, 6))
        sns.barplot(
            data=self.df,
            x="market_cap",
            y="symbol",
            palette="magma",
            hue="symbol",
        )
        plt.title("Market Capitalization of Top 10 Cryptocurrencies")
        plt.xlabel("Market Cap (USD)")
        plt.ylabel("Coin Symbol")
        plt.tight_layout()
        plt.savefig("market_cap_comparison.png")
        plt.show()