import sqlite3

def get_conn():
    return sqlite3.connect("jobs.db")

def init_db():
    conn = get_conn()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id TEXT PRIMARY KEY,
            title TEXT,
            company TEXT,
            url TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
