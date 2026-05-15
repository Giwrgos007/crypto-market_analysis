import matplotlib.pyplot as plt
import seaborn as sns


class TrendVisualizer:

    def __init__(self, dataframe):
        self.df = dataframe.sort_values(by="market_cap", ascending=False).head(
            10
        )

    def generate_chart(self):
        plt.figure(figsize=(10, 6))
        colors = [
            "green" if x > 0 else "red"
            for x in self.df["price_change_percentage_24h"]
        ]
        sns.barplot(
            data=self.df,
            x="price_change_percentage_24h",
            y="symbol",
            palette=colors,
            hue="symbol",
        )
        plt.axvline(x=0, color="black", linestyle="--", linewidth=1)
        plt.title("24h Price Trend / Performance (Top 10)")
        plt.xlabel("Price Change Percentage (24h %)")
        plt.ylabel("Coin Symbol")
        plt.tight_layout()
        plt.savefig("price_trend.png")
        plt.show()