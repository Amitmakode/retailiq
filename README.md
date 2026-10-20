# retailiq
RetailIQ: retail analytics and AI assistant project
# RetailIQ

A retail analytics command line tool built on the Olist Brazilian e-commerce dataset.

## Setup

```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python src\download_data.py
```

After downloading, copy the CSV files from the kagglehub cache into `data\raw\`.

## Usage

Run all commands from the project root.

```cmd
python -m src.main rate --base BRL --target USD
python -m src.main price --limit 5 --target USD
python -m src.main top --limit 5 --target USD
```

| Command | What it does |
| --- | --- |
| `rate` | Shows the latest exchange rate from the Frankfurter API |
| `price` | Shows order item prices converted from BRL to another currency |
| `top` | Shows top products by revenue, converted to another currency |

## Data

- Dataset: [Olist Brazilian E-Commerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- Exchange rates: [Frankfurter API](https://frankfurter.dev) (free, no API key)