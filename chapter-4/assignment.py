# Dictionary to store student data
students = {}

# Set to store all grades
all_grades = set()

# Function to add a student
def add_student(name, grades):
    students[name] = grades
    all_grades.update(grades)
    print(f"Student '{name}' added successfully!")

# Function to view all students
def view_students():
    if students:
        print("Students and their grades:")
        for name, grades in students.items():
            print(f"{name}: {grades}")
    else:
        print("No students found.")

# Function to calculate the average grade for a student
def calculate_average(name):
    if name in students:
        average = sum(students[name]) / len(students[name])
        print(f"Average grade for {name}: {average:.2f}")
    else:
        print(f"Student '{name}' not found.")

# Function to find the highest and lowest grades in the class
def find_highest_lowest():
    if all_grades:
        print(f"Highest grade in the class: {max(all_grades)}")
        print(f"Lowest grade in the class: {min(all_grades)}")
    else:
        print("No grades found.")

# Function to remove a student
def remove_student(name):
    if name in students:
        # Remove the student's grades from the set
        for grade in students[name]:
            all_grades.discard(grade)
        # Remove the student from the dictionary
        del students[name]
        print(f"Student '{name}' removed successfully!")
    else:
        print(f"Student '{name}' not found.")

# Main program loop
while True:
    print("\nStudent Grade Tracker Menu:")
    print("1. Add a student")
    print("2. View all students")
    print("3. Calculate average grade for a student")
    print("4. Find highest and lowest grades in the class")
    print("5. Remove a student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter the student's name: ")
        grades = list(map(int, input("Enter the student's grades (comma-separated): ").split(",")))
        add_student(name, grades)
    elif choice == "2":
        view_students()
    elif choice == "3":
        name = input("Enter the student's name: ")
        calculate_average(name)
    elif choice == "4":
        find_highest_lowest()
    elif choice == "5":
        name = input("Enter the student's name: ")
        remove_student(name)
    elif choice == "6":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")