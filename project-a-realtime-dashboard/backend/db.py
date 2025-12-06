import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def connect():
    return psycopg2.connect(os.getenv("DB_URL"))


def fetch(query, params=()):
    conn = None
    cur = None
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(query, params)
        rows = cur.fetchall()
        return rows
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def execute(query, params=()):
    conn = None
    cur = None
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(query, params)
        conn.commit()
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
