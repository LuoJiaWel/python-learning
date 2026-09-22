from database import get_total_expense, get_category_total

total = get_total_expense()
print(f"總支出：{total}")

breakfast_total = get_category_total("早餐")
print(f"早餐：{breakfast_total}")