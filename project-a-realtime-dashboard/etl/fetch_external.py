import requests
import json
import csv
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("etl.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)

data = None
statusCode = None


def fetch_data():
    logging.info("Fetching data from public API...")

    global data
    global statusCode

    try:
        x = requests.get(
            "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
        )
        data = json.loads(x.text)
        statusCode = x.status_code

        if statusCode != 200:
            logging.error(f"API returned error: {statusCode}")
            return

    except Exception as e:
        logging.error(f"API request failed: {e}")


def print_data():
    print("Status Code", statusCode)
    for y in data[:3]:
        print(y)


def append_data():
    if not data:
        logging.error("No data fetched.")
        return

    fields = [
        "id",
        "name",
        "current_price",
        "market_cap",
        "price_change_percentage_24h",
        "total_supply",
        "circulating_supply",
    ]
    current_dir = os.path.dirname(__file__)
    csv_path = os.path.join(current_dir, "..", "data", "raw_data.csv")
    csv_path = os.path.abspath(csv_path)

    filtered_data = [{field: item.get(field) for field in fields} for item in data]
    with open(csv_path, "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(filtered_data)


def main():
    fetch_data()
    print_data()
    append_data()


if __name__ == "__main__":
    main()

logging.info("Fetch ETL completed.")
