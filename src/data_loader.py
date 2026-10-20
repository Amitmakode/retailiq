import csv
from pathlib import Path

# Project root folder (one level above src)
RAW_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"


def read_csv(filename: str) -> list[dict]:
    """Read a CSV file from data/raw and return a list of rows (dictionaries)."""
    file_path = RAW_DIR / filename
    with open(file_path, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


if __name__ == "__main__":
    rows = read_csv("olist_order_items_dataset.csv")
    print("Total rows:", len(rows))
    print("First row:", rows[0])