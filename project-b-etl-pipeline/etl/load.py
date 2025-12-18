import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


def load(df: pd.DataFrame):
    """
    Docstring for load

    :param df: Description
    :type df: pd.DataFrame
    """
    if df.empty:
        print("df empty")
        return

    conn = psycopg2.connect(os.getenv("DB_URL"))
    cur = conn.cursor()

    try:
        for _, row in df.iterrows():
            cur.execute(
                """
                INSERT INTO clean_data(id, name, inserted_at)
                VALUES(%s,%s,NOW())
                ON CONFLICT(id) DO UPDATE 
                SET
                    name = EXCLUDED.name,
                    inserted_at = NOW()
                """,
                (str(row["id"]), row["name"]),
            )

        conn.commit()
        print("finish insert")
    finally:
        cur.close()
        conn.close()
