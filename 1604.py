items = []
receipt_number = 1

def add_item(item_name, item_cost):
    items.append((item_name, item_cost))

def print_receipt():
    global receipt_number
    
    if not items:
        print("-----")
        return
    
    total_cost = sum(cost for _, cost in items)
    
    print(f"Чек {receipt_number}. Количество товаров: {len(items)}.")
    
    for item_name, item_cost in items:
        print(f"{item_name} - {item_cost:.2f} ")

    print(f"Итого: {total_cost:.2f}")
    print("-----")
    
    items.clear()
    receipt_number += 1

