records = []

for i in range(2):

    print(f"\n=== 第 {i + 1} 筆記帳 ===")

    # 請輸入日期
    date = input("請輸入日期：")
    # 請輸入類別
    category = input("請輸入類別：")
    # 請輸入支出
    expense = int(input("請輸入支出："))
    # 請輸入備註
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
    print(record)
    total = total + record["expense"]

print(f"\n總支出：{total}元")