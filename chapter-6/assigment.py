# Custom exception for insufficient funds
class InsufficientFundsError(Exception):
    pass

# BankAccount class
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Deposit amount must be positive.")
            self.balance += amount
        except ValueError as e:
            print(f"Error: {e}")
        else:
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        finally:
            print("Deposit operation completed.")

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive.")
            if amount > self.balance:
                raise InsufficientFundsError("Insufficient funds for withdrawal.")
            self.balance -= amount
        except ValueError as e:
            print(f"Error: {e}")
        except InsufficientFundsError as e:
            print(f"Error: {e}")
        else:
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        finally:
            print("Withdrawal operation completed.")

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

# Main program loop
def main():
    account = None
    while True:
        print("\nBank Account Manager Menu:")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                initial_balance = float(input("Enter initial balance: "))
                account = BankAccount(initial_balance)
                print("Account created successfully!")
            except ValueError:
                print("Error: Invalid input. Please enter a numeric value.")
        elif choice == "2":
            if account:
                try:
                    amount = float(input("Enter deposit amount: "))
                    account.deposit(amount)
                except ValueError:
                    print("Error: Invalid input. Please enter a numeric value.")
            else:
                print("Error: No account found. Please create an account first.")
        elif choice == "3":
            if account:
                try:
                    amount = float(input("Enter withdrawal amount: "))
                    account.withdraw(amount)
                except ValueError:
                    print("Error: Invalid input. Please enter a numeric value.")
            else:
                print("Error: No account found. Please create an account first.")
        elif choice == "4":
            if account:
                account.check_balance()
            else:
                print("Error: No account found. Please create an account first.")
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()