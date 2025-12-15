import psycopg2
import csv
import os
from dotenv import load_dotenv
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("etl.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)

load_dotenv()


def load_csv():
    rows = []
    current_dir = os.path.dirname(__file__)
    csv_path = os.path.join(current_dir, "..", "data", "raw_data.csv")
    csv_path = os.path.abspath(csv_path)

    with open(csv_path, "r", encoding="utf-8") as csvfile:
        csvreader = csv.DictReader(csvfile)

        for row in csvreader:
            rows.append(row)

    logging.info(f"Loaded {len(rows)} rows from CSV.")
    return rows


def insert_into_db(rows):
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    cur = conn.cursor()

    logging.info(f"Starting insert for {len(rows)} rows")

    query = """
        INSERT INTO coins(
        id, name, current_price, market_cap, price_change_percentage_24h, total_supply, circulating_supply
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (id)
        DO UPDATE SET
            current_price = EXCLUDED.current_price,
            market_cap = EXCLUDED.market_cap,
            price_change_percentage_24h = EXCLUDED.price_change_percentage_24h;

  ;
    """

    success = 0
    for row in rows:
        try:
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
            success += 1
        except Exception as e:
            conn.rollback()
            logging.error(f"Insert failed for row {row.get('id')}: {e}")

    conn.commit()
    cur.close()
    conn.close()
    logging.info("Insert completed {success} rows")


def main():
    rows = load_csv()

    if not rows:
        logging.warning("No data to insert")
        return

    insert_into_db(rows)


if __name__ == "__main__":
    main()
