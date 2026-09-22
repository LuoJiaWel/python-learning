import sqlite3

connection = sqlite3.connect("money_tracker.db")
#----------------------------------------------------------------
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
#----------------------------------------------------------------
def add_record(date, category, expense, remark):
    connection.execute("""
    INSERT INTO records (date, category, expense, remark)
    VALUES (?, ?, ?, ?)
    """, (date, category, expense, remark))

    connection.commit()
#----------------------------------------------------------------
def get_records():
    result = connection.execute("""
    SELECT * FROM records
    """).fetchall()

    records = []

    for record in result:
        id, date, category, expense, remark = record

        records.append({
            "id": id,
            "date": date,
            "category": category,
            "expense": expense,
            "remark": remark
        })

    return records
#----------------------------------------------------------------
def update_record(record_id, date, category, expense, remark):
    connection.execute("""
    UPDATE records
    SET date = ?, category = ?, expense = ?, remark = ?
    WHERE id = ?
    """, (date, category, expense, remark, record_id))

    connection.commit()
#----------------------------------------------------------------
def delete_record_from_database(record_id):
    connection.execute("""
    DELETE FROM records
    WHERE id = ?
    """, (record_id,))

    connection.commit()
#----------------------------------------------------------------
def get_total_expense():
    result = connection.execute("""
    SELECT SUM(expense)
    FROM records
    """).fetchone()

    return result[0] or 0
#----------------------------------------------------------------
def get_category_total(category):
    result = connection.execute("""
    SELECT SUM(expense)
    FROM records
    WHERE category = ?
    """, (category,)).fetchone()

    return result[0] or 0
#----------------------------------------------------------------