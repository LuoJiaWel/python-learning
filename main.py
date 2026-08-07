records = []

for i in range(2):

    print(f"\n=== 第 {i + 1} 筆記帳 ===")

    date = input("請輸入日期：")
    category = input("請輸入類別：")
    expense = int(input("請輸入支出："))
    remark = input("請輸入備註：")

    record = {
        "date" : date,
        "category" : category,
        "expense" : expense,
        "remark" : remark
    }
    records.append(record)

total = 0

print("\n所有記帳資料：")

for record in records:
    print(f"日期：{record['date']}")
    print(f"類別：{record['category']}")
    print(f"支出：{record['expense']}")
    print(f"備註：{record['remark']}")

    total = total + record['expense']

    print()

print(f"\n總支出：{total}元")