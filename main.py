from test import delete_record


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

def delete_record(records):

    if len(records) == 0:
        print("目前沒有任何記帳資料可以刪除")
        return

    print("\n所有記帳資料：")

    for i, record in enumerate(records):
        print(f"{i + 1} 筆")
        print(f"日期：{record['date']}")
        print(f"類別:{record['category']}")
        print(f"支出:{record['expense']}")
        print(f"備註:{record['remark']}")
        print()

    choice = int(input("請輸入要刪除的編號："))

    if choice == 1 and choice <= len(records):
        index = choice - 1
        del records[index]
        print("刪除成功!")

    else:
        print("無效的編號。")


records = []

while True:
    print("\n==== 記帳系統 ====")
    print("1. 新增記帳")
    print("2. 查看記帳")
    print("3. 查看總支出")
    print("4. 刪除記帳")
    print("4. 離開")

    choice = input("\n請選擇：")

    if choice == "1":
        input_record(records)

    elif choice == "2":
        show_records(records)

    elif choice == "3":
        total = calculate_total(records)
        print(f"總支出:{total}")

    elif choice == "4":
        delete_record(records)

    elif choice == "5":
        print("離開程式")
        break

    else:
        print("\n無效的選擇，請重新輸入。")