import requests
import json
import csv
import os

data = None
statusCode = None


def fetch_data():
    x = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd")
    global data
    global statusCode

    data = json.loads(x.text)
    statusCode = x.status_code


def print_data():
    print("Status Code", statusCode)
    for y in data[:3]:
        print(y)


def append_data():
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


fetch_data()
print_data()
append_data()
