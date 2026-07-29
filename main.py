name = input("請輸入姓名")

income = int(input("請輸入今天收入："))

expense = int(input("請輸入今天支出："))

balance = income - expense

if balance >= 0:
    print(f"{name}，你今天剩餘 {balance} 元")
elif balance == 0:
    print(f"{name}，你今天剛好打平")
else:
    print(f"{name}，今天超支{abs(balance)}")