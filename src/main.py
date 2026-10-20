import argparse

from src.data_loader import read_csv
from src.fx_rate import get_rate
from src.analytics import top_products


def show_prices(limit: int, target: str) -> None:
    """Show order item prices in BRL and in the target currency."""
    rate = get_rate("BRL", target)
    rows = read_csv("olist_order_items_dataset.csv")[:limit]

    print(f"Rate: 1 BRL = {rate} {target}")
    for row in rows:
        price_brl = float(row["price"])
        price_target = round(price_brl * rate, 2)
        print(f"Order {row['order_id'][:8]} | {price_brl:.2f} BRL = {price_target:.2f} {target}")


def show_top(limit: int, target: str) -> None:
    """Show top products by revenue in BRL and in the target currency."""
    rate = get_rate("BRL", target)
    print(f"Rate: 1 BRL = {rate} {target}")
    for position, (product_id, total) in enumerate(top_products(limit), start=1):
        print(f"{position}. {product_id[:8]} | {total:.2f} BRL = {total * rate:.2f} {target}")


def main():
    parser = argparse.ArgumentParser(prog="retailiq", description="RetailIQ command line tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # "rate" command: show the latest exchange rate
    rate_parser = subparsers.add_parser("rate", help="Show latest exchange rate")
    rate_parser.add_argument("--base", default="BRL", help="Base currency (default: BRL)")
    rate_parser.add_argument("--target", default="USD", help="Target currency (default: USD)")

    # "price" command: show order item prices converted to another currency
    price_parser = subparsers.add_parser("price", help="Show order item prices in another currency")
    price_parser.add_argument("--limit", type=int, default=5, help="Number of rows to show (default: 5)")
    price_parser.add_argument("--target", default="USD", help="Target currency (default: USD)")


    # "top" command: show top products by revenue
    top_parser = subparsers.add_parser("top", help="Show top products by revenue")
    top_parser.add_argument("--limit", type=int, default=5, help="Number of products (default: 5)")
    top_parser.add_argument("--target", default="USD", help="Target currency (default: USD)")

    args = parser.parse_args()

    if args.command == "rate":
        rate = get_rate(args.base, args.target)
        print(f"1 {args.base} = {rate} {args.target}")
    elif args.command == "price":
        show_prices(args.limit, args.target)
    elif args.command == "top":
        show_top(args.limit, args.target)


if __name__ == "__main__":
    main()