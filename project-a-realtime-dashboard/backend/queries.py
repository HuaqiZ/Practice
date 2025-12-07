from db import fetch, execute


def get_latest_price(symbol: str):
    rows = fetch("SELECT id, current_price FROM coins WHERE id = %s", (symbol,))
    if not rows:
        return None
    row = rows[0]
    return {"id": row[0], "current_price": row[1]}


def delete_coin(symbol: str):
    execute("DELETE FROM coins WHERE id = %s", (symbol,))
