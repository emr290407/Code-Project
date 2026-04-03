# Menu Display
print("- - - - - - - - - - - - - - - - - - - - -")
print("|  Grade  |  A  |  B  |  C  |  D  |  E  |")
print("- - - - - - - - - - - - - - - - - - - - -")
print("|  Points |  4  |  3  |  2  |  1  |  0  |")
print("- - - - - - - - - - - - - - - - - - - - -")

# Data Storage
menu_data = {
    "A": 4,
    "B": 3,
    "C": 2,
    "D": 1,
    "E": 0,
}

# User Input
grade = input("Enter grade of the subject: ").upper() 

# Calculation and Output
if grade in menu_data:
    score = menu_data[grade]
    
    print(f"Points Obtained: {score:.2f}")
else:
    print("Invalid Grade. Please enter A, B, C, D, or E.")