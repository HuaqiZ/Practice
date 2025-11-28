import csv
import os

current_dir = os.path.dirname(__file__)
csv_path = os.path.join(current_dir, "..", "data", "raw_data.csv")
csv_path = os.path.abspath(csv_path)
rows = []

with open(csv_path, "r") as csvfile:
    csvreader = csv.DictReader(csvfile)

    for row in csvreader:
        rows.append(row)


def analyze():
    total = 0
    for row in rows:
        total += float(row["current_price"])
    average = total / len(rows)
    print(average)


analyze()
