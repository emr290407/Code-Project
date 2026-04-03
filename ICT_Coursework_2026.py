# Menu Display
print("                           Room   Capacity                           ")
print("Package          Double       Triple       Quad                      ")
print("                  (RM)         (RM)        (RM)                      ")
print("Premium          14,500       13,500      12,500                     ")
print("Medium           12,300       11,600      10,900                     ")
print("Budget            9,200        8,200       7,900                     ")
print("                                                                     ")

# Data Storage 
menu_data = {
    1: {"name": "Premium", 1: 14500.00, 2: 13500.00, 3: 12500.00},
    2: {"name": "Medium",  1: 12300.00, 2: 11600.00, 3: 10900.00},
    3: {"name": "Budget",  1: 9200.00,  2: 8200.00,  3: 7900.00},
}

try:
    # User Input
    user_choice = int(input("Please choose package (1)Premium (2)Medium (3)Budget : "))
    user_capacity = int(input("Please choose room capacity (1)Double (2)Triple (3)Quad : "))
    quantity = int(input("Number of pax : "))

    # Calculation and Output
    if user_choice in menu_data and user_capacity in menu_data[user_choice]:
        # Retrieve data
        package_info = menu_data[user_choice]
        unit_price = package_info[user_capacity]
        package_name = package_info["name"]
        
        total_price = unit_price * quantity
        
        print(f"Total charge for {quantity} pax: RM {total_price:,.2f}")
    else:
        print("\nError: Invalid package or capacity selection.")
        
except ValueError:
    print("\nError: Please enter numbers only for selection and quantity.")