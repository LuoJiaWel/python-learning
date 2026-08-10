records = []

def input_record():
    print(f"\n=== 第 {i + 1} 筆記帳 ===")

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

def show_records():
    total = 0
    print("\n所有記帳資料：")

    for record in records:
        print(record)
        total = total + record["expense"]

    print(f"\n總支出：{total}元")


for i in range(2):
    input_record()
    show_records()