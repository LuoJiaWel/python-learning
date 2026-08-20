def input_record(records):
    date = input("請輸入日期：")
    category = input("請輸入類別：")

    expense = input_expense()

    remark = input("請輸入備註：")

    record = {
        "date": date,
        "category": category,
        "expense": expense,
        "remark": remark
    }

    records.append(record)


def input_expense():
    while True:
        try:
            expense = float(input("請輸入支出："))

        except ValueError:
            print("輸入無效，請輸入數字。")
            continue

        if expense < 0:
            print("輸入無效，支出不能是負數。")
            continue

        return expense



def show_records(records):
    print("\n所有記帳資料：")

    for i, record in enumerate(records):
        print(f"第 {i + 1} 筆")
        print(f"日期:{record['date']}")
        print(f"類別:{record['category']}")
        print(f"支出:{format_amount(record['expense'])}元")
        print(f"備註:{record['remark']}")
        print()


def calculate_total(records):

    total = 0

    for record in records:
        total += record["expense"]

    return total

def format_amount(amount):
    if amount == int(amount):
        return str(int(amount))
    else:
        return str(amount)

def delete_record(records):

    if len(records) == 0:
        print("目前沒有任何記帳資料可以刪除。")
        return

    print("\n所有記帳資料：")

    for i, record in enumerate(records):
        print(f"第 {i + 1} 筆")
        print(f"日期:{record['date']}")
        print(f"類別:{record['category']}")
        print(f"支出：{format_amount(record['expense'])}元")
        print(f"備註:{record['remark']}")
        print()
    while True:
        choice = input("請輸入記帳編號，或按 q 取消刪除：")

        if choice == "q":
            print("取消刪除。")
            return

        try:
            choice = int(choice)

        except ValueError:
            print("請輸入數字。")
            continue

        if choice >= 1 and choice <= len(records):
            index = choice - 1
            del records[index]
            print("刪除成功!")
            break
        else:
            print("無效的編號。")
            continue


records = []

while True:
    print("\n==== 記帳系統 ====")
    print("1. 新增記帳")
    print("2. 查看記帳")
    print("3. 查看總支出")
    print("4. 刪除記帳")
    print("5. 離開")

    choice = input("\n請選擇：")

    if choice == "1":
        input_record(records)

    elif choice == "2":
        show_records(records)

    elif choice == "3":
        total = calculate_total(records)
        print(f"總支出：{format_amount(total)}元")

    elif choice == "4":
        delete_record(records)

    elif choice == "5":
        print("已離開程式，感謝使用。")
        break

    else:
        print("\n無效的選擇，請重新輸入。")