def input_record(records):
    date = input("請輸入日期：")
    category = input("請輸入類別：")
    expense = int(input("請輸入支出："))
    remark = input("請輸入備註：")

    record = {
        "date": date,
        "category": category,
        "expense": expense,
        "remark": remark
    }
    records.append(record)


def show_records(records):
    print("\n所有記帳資料：")

    for record in records:
        print(f"日期:{record['date']}")
        print(f"類別:{record['category']}")
        print(f"支出:{record['expense']}")
        print(f"備註:{record['remark']}")
        print()


def calculate_total(records):

    total = 0

    for record in records:
        total += record["expense"]

    return total


records = []

for i in range(2):
    print(f"\n=== 第 {i + 1} 筆記帳 ===")

    input_record(records)

show_records(records)

total = calculate_total(records)

print(f"總支出：{total}元")