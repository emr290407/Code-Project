total_price = 0.0
counter = 1
choice = 'Y'

# Display Header and Menu
print("       XYZ Auto Tyres and Services SDN. BHD.")
print("-" * 54)
print("           Item for services and spare parts")
print(f"{'Item Code':<15} {'Description':<25} {'Price':<10}")
print(f"{'1':<15} {'Tyre alignment':<25} {'25.00':<10}")
print(f"{'2':<15} {'Tyre balancing':<25} {'5.50':<10}")
print(f"{'3':<15} {'New tyre':<25} {'200.00':<10}")
print(f"{'4':<15} {'Engine oil (inclusive)':<25} {'150.00':<10}")
print(f"{'5':<15} {'Engine tuning':<25} {'80.00':<10}")
print(f"{'6':<15} {'Brake service':<25} {'30.00':<10}\n")

while choice.upper() == 'Y':
    print(f"No.{counter}")
    
    item_code = int(input("Enter item code    : "))
    quantity = int(input("Enter quantity     : "))

    # Pricing Logic
    if item_code == 1:
        unit_price = 25.00
    elif item_code == 2:
        unit_price = 5.50
    elif item_code == 3:
        unit_price = 200.00
    elif item_code == 4:
        unit_price = 150.00
    elif item_code == 5:
        unit_price = 80.00
    elif item_code == 6:
        unit_price = 30.00
    else:
        unit_price = 0.0
        print("Invalid item code!")

    sub_total = unit_price * quantity
    total_price += sub_total

    print(f"Item price         : RM {sub_total:.2f}")
    choice = input("Any more item(Y/N) : ")
    print() 
    counter += 1

print("-" * 54)
print(f"Total price        : RM {total_price:.2f}")
print("-" * 54)