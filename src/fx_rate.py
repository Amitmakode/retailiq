import requests

API_URL = "https://api.frankfurter.dev/v1/latest"


def get_rate(base: str, target: str) -> float:
    """Return the latest exchange rate from base currency to target currency."""
    params = {"base": base, "symbols": target}
    try:
        response = requests.get(API_URL, params=params, timeout=10)
        # Raises an error for 4xx/5xx status codes
        response.raise_for_status()
        return response.json()["rates"][target]
    except requests.exceptions.RequestException as error:
        raise RuntimeError(f"Could not fetch exchange rate: {error}")


if __name__ == "__main__":
    print("BRL to USD:", get_rate("BRL", "USD"))