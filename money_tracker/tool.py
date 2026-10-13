#這個函式的功用是 "把金額整理成「顯示用的格式」" 希望回傳的都是字串
#因為使用float()，使用者輸入100會顯示100.0
#但我希望顯示整數是100，所以用這個函式

def format_amount(amount):
    if amount == int(amount):
        return str(int(amount))  #這個不套用str會回傳整數
    else:
        return str(amount) #這個不套用str可能會回傳浮點數