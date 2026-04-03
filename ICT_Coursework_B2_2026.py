def main():
    total_charge = 0
    more_booking = 'y'

    while more_booking.lower() == 'y':
        print("\n            Room Capacity")
        print("Package     Double    Triple    Quad")
        print("            (RM)      (RM)      (RM)")
        print("Premium     14,500    13,500    12,500")
        print("Medium      12,300    11,600    10,900")
        print("Budget      9,200     8,200     7,900\n")

        package = int(input("Please choose package (1) Premium (2) Medium (3) Budget : "))
        capacity = int(input("Please choose room capacity (1) Double (2) Triple (3) Quad : "))
        pax = int(input("Number of pax: "))

        # Price Logic
        if package == 1: 
            rates = [14500, 13500, 12500]
        elif package == 2: 
            rates = [12300, 11600, 10900]
        elif package == 3:  
            rates = [9200, 8200, 7900]
        else:
            print("")
            print("Invalid Code. If you want a room then what is so hard to enter the correct code? Haiyaaa!!")
            main()

        rate = rates[capacity - 1]
        package_charge = rate * pax
        total_charge += package_charge

        print(f"\nPackage charge is RM {package_charge}")
        more_booking = input("\nMore booking? (Y/N) : ")

    print(f"\nTotal charge for customer is RM {total_charge}")

if __name__ == "__main__":
    main()