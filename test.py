from database import add_record, get_records

add_record("2026-09-18", "早餐", 60, "蛋餅")

records = get_records()

print(records)