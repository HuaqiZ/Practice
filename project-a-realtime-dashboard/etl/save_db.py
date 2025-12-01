import psycopg2
import csv
import os
from dotenv import load_dotenv

load_dotenv()

rows = []


def load_csv():
    current_dir = os.path.dirname(__file__)
    csv_path = os.path.join(current_dir, "..", "data", "raw_data.csv")
    csv_path = os.path.abspath(csv_path)
    global rows

    with open(csv_path, "r", encoding="utf-8") as csvfile:
        csvreader = csv.DictReader(csvfile)

        for row in csvreader:
            rows.append(row)


def insert_into_db():
    conn = psycopg2.connect(os.getenv("DB_URL"))
    cur = conn.cursor()

    query = """
        INSERT INTO coins(
        id, name, current_price, market_cap, price_change_percentage_24h, total_supply, circulating_supply
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s);
    """
    for row in rows:
        cur.execute(
            query,
            (
                row["id"],
                row["name"],
                float(row["current_price"]) if row["current_price"] else None,
                row["market_cap"],
                row["price_change_percentage_24h"],
                row["total_supply"],
                row["circulating_supply"],
            ),
        )

    conn.commit()
    cur.close()
    conn.close()
    print("Inserted into DB successfully!")


load_csv()
insert_into_db()
