# Menu Display
print("                                  XYZ Auto Tyres and Service SDN. BHD.                                  ")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
print("                                   Item for services and spare parts                                    ")
print("                                                                                                        ")
print("                     Item Code                Description                Price                          ")
print("                     1                        Tyre alignment             25.00                          ")
print("                     2                        Tyre balancing             5.50                           ")
print("                     3                        New tyre                   200.00                         ")
print("                     4                        Engine oil (inclusive)     150.00                         ")
print("                     5                        Engine tuning              80.00                          ")
print("                     6                        Brake service              30.00                          ")
print("                                                                                                        ")

# Data Storage 
menu_data = {
    1: {"description": "Tyre alignment",          "price": 25.00},
    2: {"description": "Tyre balancing",          "price": 5.50},
    3: {"description": "New tyre",                "price": 200.00},
    4: {"description": "Engine oil (inclusive)",  "price": 150.00},
    5: {"description": "Engine tuning",           "price": 80.00},
    6: {"description": "Brake service",           "price": 30.00},
}

# User Input
try:
    item_code = int(input("\t\tEnter Item Code          : "))
    quantity = int(input("\t\tEnter Quantity           : "))

    # Calculation and Output
    if item_code in menu_data:
        unit_price = menu_data[item_code]["price"]
        service = menu_data[item_code]["description"]
        
        total_price = unit_price * quantity
        
        print(f"\t\tTotal Price              : RM {total_price:.2f}")
    else:
        print("\nError: Invalid Item Code. Please restart the program.")
        
except ValueError:
    print("\nError: Please enter numbers only for Item Code and Quantity.")