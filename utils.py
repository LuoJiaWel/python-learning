#因為使用float()，使用者輸入100會顯示100.0
#但我希望顯示整數是100，所以用這個函式

def format_amount(amount):
    if amount == int(amount):
        return str(int(amount))
    else:
        return str(amount)