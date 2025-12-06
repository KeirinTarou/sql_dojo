from pathlib import Path
import sqlite3
from sql_dojo.config import DATA_DIR

DB_PATH = DATA_DIR / "practice.db"

def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn