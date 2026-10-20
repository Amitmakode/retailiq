from collections import defaultdict

from src.data_loader import read_csv


def top_products(limit: int = 5) -> list[tuple[str, float]]:
    """Return top products by total revenue (BRL) from order items."""
    revenue = defaultdict(float)

    for row in read_csv("olist_order_items_dataset.csv"):
        revenue[row["product_id"]] += float(row["price"])

    # Sort by revenue, highest first, and keep only the top N
    ranked = sorted(revenue.items(), key=lambda item: item[1], reverse=True)
    return ranked[:limit]


if __name__ == "__main__":
    for product_id, total in top_products():
        print(product_id[:8], "|", round(total, 2), "BRL")