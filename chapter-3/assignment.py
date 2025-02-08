conversion_count = 0

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

def display_menu():
    """Display the menu options"""
    print("\nTemperature Converter Tool")
    print("1) Convert Celsius to Fahrenheit")
    print("2) Convert Fahrenheit to Celsius")
    print("3) Exit")

def main():
    """Main program logic"""
    global conversion_count

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Convert Celsius to Fahrenheit
            try:
                celsius = float(input("Enter the temperature in Celsius: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
                conversion_count += 1
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '2':
            # Convert Fahrenheit to Celsius
            try:
                fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
                conversion_count += 1
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '3':
            # Exit the program
            print(f"Total conversions performed: {conversion_count}")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()