import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "agentrewind.db"

def connect() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS runs (id TEXT PRIMARY KEY, payload TEXT)"
    )
    return conn
