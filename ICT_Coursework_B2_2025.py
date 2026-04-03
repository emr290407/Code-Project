# Display the grade reference table
print("-" * 43)
print("| Grade  |  A  |  B  |  C  |  D  |  E  |")
print("| Points |  4  |  3  |  2  |  1  |  0  |")
print("-" * 43)

# Initialize variables
total_points = 0.0
grade_map = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'E': 0.0}

# Repetition Control Structure (Loop for 4 subjects)
for i in range(1, 5):
    grade_input = input(f"\n{i}. Enter grade of the subject : ").upper()
    
    # Get points from dictionary, default to 0.0 if grade not found
    points = grade_map.get(grade_input, 0.0)
    
    print(f"   Points obtain             : {points:.2f}")
    total_points += points

# Calculate Academic Merit (Average of 4 subjects)
academic_merit = total_points / 4.0

# Input Co-curricular merit
co_curricular = float(input("\n   Enter the co-curricular merit : "))
print(f"   Co-curricular merit       : {co_curricular:.2f}")

# Calculate Total Merit based on the formula:
# (academic_merit / 4) * 90 + co_curricular
total_merit = (academic_merit / 4.0) * 90 + co_curricular

# Final Display
print("-" * 43)
print(f"   Academic merit            : {academic_merit:.2f}")
print(f"   Total merit points        : {total_merit:.2f}")