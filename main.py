name = input("請輸入姓名")

income = int(input("請輸入今天收入："))

expense = int(input("請輸入今天支出："))

balance = income - expense

print(f"{name}，你今天剩餘 {balance} 元")