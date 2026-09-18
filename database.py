import sqlite3

connection = sqlite3.connect("money_tracker.db")

def add_record(date, category, expense, remark):
    connection.execute("""
    INSERT INTO records (date, category, expense, remark)
    VALUES (?, ?, ?, ?)
    """, (date, category, expense, remark))

    connection.commit()


add_record("2026-09-17", "午餐", 120, "便當")

result = connection.execute("SELECT * FROM records").fetchall()

print(result)
