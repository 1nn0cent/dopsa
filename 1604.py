items = []
receipt_number = 1

def add_item(item_name, item_cost):
    items.append((item_name, item_cost))

def print_receipt():
    global receipt_number
    
    if not items:
        return
    
    total_cost = sum(cost for _, cost in items)
    
    print(f"Чек {receipt_number}. Всего предметов: {len(items)}")
    
    for item_name, item_cost in items:
        print(f"{item_name} - {item_cost:} ")

    print(f"Итого: {total_cost:}")
    print("-----")
    
    items.clear()
    receipt_number += 1
add_item('Блокнот', 100)
print_receipt()
add_item('Ручка', 70)
print_receipt()
print_receipt()
add_item('Булочка', 15)
add_item('Булочка', 15)
add_item('Чай', 5)
print_receipt()
