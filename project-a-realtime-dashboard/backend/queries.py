from db import fetch, execute


def get_latest_price(symbol: str):
    rows = fetch("SELECT id, name, current_price FROM coins WHERE id = %s", (symbol,))
    if not rows:
        return None
    row = rows[0]
    return {"id": row[0], "name": row[1], "current_price": row[2]}


def get_all_price():
    rows = fetch("SELECT id, name, current_price FROM coins")
    if not rows:
        return None
    return [{"id": row[0], "name": row[1], "current_price": row[2]} for row in rows]


def delete_coin(symbol: str):
    execute("DELETE FROM coins WHERE id = %s", (symbol,))
