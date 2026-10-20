import json
from pathlib import Path

from src.analytics import top_products

# Output folder: data/output (created automatically if missing)
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "data" / "output"


def save_json(data, filename: str) -> Path:
    """Save data as a JSON file in data/output and return the file path."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    file_path = OUTPUT_DIR / filename
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
    return file_path


def load_json(filename: str):
    """Load a JSON file from data/output and return its content."""
    with open(OUTPUT_DIR / filename, encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":
    data = [
        {"product_id": product_id, "revenue_brl": round(total, 2)}
        for product_id, total in top_products(3)
    ]
    path = save_json(data, "top_products.json")
    print("Saved to:", path)
    print("Loaded back:", load_json("top_products.json"))