from database import (
    add_record,
    get_records,
    update_record,
    delete_record_from_database
)

#utils翻譯成工具
from utils import format_amount

from record import (
    input_record,
    show_records,
    calculate_total,
    delete_record,
    calculate_category_total,
    choose_category,
    edit_record
)

if __name__ == "__main__":

    #主程式_主要操作地方
    while True:
        print("\n==== 記帳系統 ====")
        print("1. 新增記帳")
        print("2. 查看記帳")
        print("3. 查看總支出")
        print("4. 刪除記帳")
        print("5. 查看類別總支出")
        print("6. 修改記帳")
        print("7. 離開")

        choice = input("\n請選擇：")

        if choice == "1":
            date, category, expense, remark = input_record()
            add_record(date, category, expense, remark)

        elif choice == "2":
            records = get_records()
            show_records(records)

        elif choice == "3":
            records = get_records()
            total = calculate_total(records)
            print(f"總支出：{format_amount(total)}元")

        elif choice == "4":
            records = get_records()
            deleted = delete_record(records)

            if deleted is not None:
                delete_record_from_database(deleted["id"])


        elif choice == "5":
            records = get_records()
            category = choose_category(records)

            if category is None:
                continue

            total, found = calculate_category_total(records, category)

            if found:
                print(f"{category}總支出：{format_amount(total)}元")
            else:
                print(f"找不到「{category}」的記帳資料。")

        elif choice == "6":
            records = get_records()
            modified = edit_record(records)

            if modified is not None:
                update_record(
                    modified["id"],
                    modified["date"],
                    modified["category"],
                    modified["expense"],
                    modified["remark"]
                )


        elif choice == "7":
            print("已離開程式，感謝使用。")
            break


        else:
            print("\n無效的選擇，請重新輸入。")



