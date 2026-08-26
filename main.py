import json

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


def show_record(record):
    print(f"日期：{record['date']}")
    print(f"類別：{record['category']}")
    print(f"支出：{format_amount(record['expense'])}元")
    print(f"備註：{record['remark']}")
    print()


def show_records(records):
    print("\n所有記帳資料：")

    for i, record in enumerate(records):
        print(f"第 {i + 1} 筆")
        show_record(record)


def calculate_total(records):

    total = 0

    for record in records:
        total += record["expense"]

    return total

def delete_record(records):

    if len(records) == 0:
        print("目前沒有任何記帳資料可以刪除。")
        return False

    print("\n所有記帳資料：")

    for i, record in enumerate(records):
        print(f"第 {i + 1} 筆")
        show_record(record)

    while True:
        choice = input("請輸入記帳編號，或按 q 取消刪除：")

        if choice == "q":
            print("取消刪除。")
            return False

        try:
            choice = int(choice)

        except ValueError:
            print("請輸入數字。")
            continue

        if 1 <= choice <= len(records):
            index = choice - 1
            del records[index]
            print("刪除成功!")
            return True
        else:
            print("無效的編號。")
            continue


def format_amount(amount):
    if amount == int(amount):
        return str(int(amount))
    else:
        return str(amount)


def load_records():
    try:
        with open("records.json", "r") as file:
            records = json.load(file)
        return records
    except FileNotFoundError:
        return []


def save_records(records):
    with open("records.json", "w") as file:
        json.dump(records, file)

def calculate_category_total(records, category):
    total = 0
    found = False

    for record in records:
        if record["category"] == category:
            total += record["expense"]
            found = True

    return total, found

def get_categories(records):
    caregories = set()

    for record in records:
        caregories.add(record["category"])

    return caregories

def choose_category(records):
    if len(records) == 0:
        print("目前沒有任何記帳資料。")
        return None

    categories = sorted(get_categories(records))

    print("\n目前的類別：")

    for i, category in enumerate(categories):
        print(f"{i + 1}. {category}")

    while True:
        choice = input("請選擇類別：")

        try:
            choice = int(choice)
        except ValueError:
            print("請輸入數字。")
            continue
        if 1 <= choice <= len(categories):
            index = choice - 1
            return categories[index]
        else:
            print("無效的選擇。")


records = load_records()

while True:
    print("\n==== 記帳系統 ====")
    print("1. 新增記帳")
    print("2. 查看記帳")
    print("3. 查看總支出")
    print("4. 刪除記帳")
    print("5. 查看類別總支出")
    print("6. 離開")

    choice = input("\n請選擇：")

    if choice == "1":
        input_record(records)
        save_records(records)

    elif choice == "2":
        show_records(records)

    elif choice == "3":
        total = calculate_total(records)
        print(f"總支出：{format_amount(total)}元")

    elif choice == "4":
        deleted = delete_record(records)

        if deleted:
            save_records(records)


    elif choice == "5":
        category = choose_category(records)

        if category is None:
            continue

        total, found = calculate_category_total(records, category)

        if found:
            print(f"{category}總支出：{format_amount(total)}元")
        else:
            print(f"找不到「{category}」的記帳資料。")


    elif choice == "6":
        print("已離開程式，感謝使用。")
        break


    else:
        print("\n無效的選擇，請重新輸入。")