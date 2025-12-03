from db import fetch, execute


def get_latest_price(symbol: str):
    rows = fetch("SELECT id, current_price FROM coins WHERE id = %s", (symbol,))
    print(rows)

def delete_coin(symbol: str):
    execute("DELETE FROM coins WHERE id = %s", (symbol,))


get_latest_price("tether")
delete_coin("bitcoin")
