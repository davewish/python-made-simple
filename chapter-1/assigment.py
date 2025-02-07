# Step 1: Prompt the user for input
score = input("Enter the student's score: ")

# Step 2: Convert input to a number
score = float(score)

# Step 3: Determine the grade
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Step 4: Display the grade
print(f"The student's grade is: {grade}")