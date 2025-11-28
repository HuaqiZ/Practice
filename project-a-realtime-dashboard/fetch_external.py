import requests
import json
import csv

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
    filename = "raw_data.csv"

    filtered_data = [{field: item.get(field) for field in fields} for item in data]
    with open(filename, "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(filtered_data)


fetch_data()
print_data()
append_data()
