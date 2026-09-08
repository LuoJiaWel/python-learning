from utils import format_amount

#負責給使用者輸入資料
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

#輸入支出
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

#顯示「一筆」紀錄
def show_record(record):
    print(f"日期：{record['date']}")
    print(f"類別：{record['category']}")
    print(f"支出：{format_amount(record['expense'])}元")
    print(f"備註：{record['remark']}")
    print()

#顯示整筆List
def show_records(records):
    print("\n所有記帳資料：")

    for i, record in enumerate(records):
        print(f"第 {i + 1} 筆")
        show_record(record)

#負責計算總額
def calculate_total(records):

    total = 0

    for record in records:
        total += record["expense"]

    return total

#負責計算「類別的總額」並回傳結果
def calculate_category_total(records, category):
    total = 0
    found = False

    for record in records:
        if record["category"] == category:
            total += record["expense"]
            found = True

    return total, found

#刪除紀錄
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


# 選擇要要編輯的紀錄
def edit_record(records):

    if len(records) == 0:
        print("目前沒有任何記帳資料可以修改。")
        return False

    print("\n所有記帳資料：")

    for i,record in enumerate(records):
        print(f"第 {i + 1} 筆")
        show_record(record)
        print()

    while True:
        choice = input("請輸入要修改的記帳編號，或按 q 取消：")

        if choice == "q":
            print("取消修改。")
            return False

        try:
            choice = int(choice)

        except ValueError:
            print("請輸入數字。")
            continue

        if 1 <= choice <= len(records):
            index = choice - 1
            record = records[index]
            break

        else:
            print("無效的編號。")

    while True:
        print("\n要修改什麼？")
        print("1. 日期")
        print("2. 類別")
        print("3. 支出")
        print("4. 備註")
        print("5. 取消")

        choice = input("請選擇：")

        if choice == "1":
            record["date"] = input("請輸入新的日期：")
            print("修改成功！")
            return True

        elif choice == "2":
            record["category"] = input("請輸入新的類別：")
            print("修改成功！")
            return True

        elif choice == "3":
            record["expense"] = input_expense()
            print("修改成功！")
            return True

        elif choice == "4":
            record["remark"] = input("請輸入新的備註：")
            print("修改成功！")
            return True

        elif choice == "5":
            print("取消修改。")
            return False

        else:
            print("無效的選擇。")

#取得「不重複類別」_使用了set()
def get_categories(records):
    categories  = set()

    for record in records:
        categories.add(record["category"])

    return categories

#資料排序_使用了sorted()
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
