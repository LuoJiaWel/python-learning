from database import get_records, update_record

update_record(1, "2026/9/21", "food", 200, "修改測試")

records = get_records()

print(records)