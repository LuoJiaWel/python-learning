import sqlite3

connection = sqlite3.connect("money_tracker.db")

def initialize_database():
    connection.execute("""
    CREATE TABLE IF NOT EXISTS records (
        id INTEGER PRIMARY KEY,
        date TEXT,
        category TEXT,
        expense REAL,
        remark TEXT
    )
    """)

    connection.commit()

def add_record(date, category, expense, remark):
    connection.execute("""
    INSERT INTO records (date, category, expense, remark)
    VALUES (?, ?, ?, ?)
    """, (date, category, expense, remark))

    connection.commit()

def get_records():
    result = connection.execute("""
    SELECT * FROM records
    """).fetchall()

    return result