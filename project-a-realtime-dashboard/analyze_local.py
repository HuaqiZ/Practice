import csv

filename = "raw_data.csv"
rows = []

with open(filename, "r") as csvfile:
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
