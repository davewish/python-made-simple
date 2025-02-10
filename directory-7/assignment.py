import os
from datetime import datetime

JOURNAL_FILE = "journal_entries.txt"


def display_menu():
    print("\n=== Personal Journal App ===")
    print("1. Write a new journal entry")
    print("2. View all journal entries")
    print("3. Search for a specific entry")
    print("4. Exit")


def write_entry():
    """Write a new journal entry."""
    entry = input("\nWrite your journal entry: ")
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(JOURNAL_FILE, "a") as file:
        file.write(f"[{current_time}] {entry}\n")
    print("Entry added successfully!")


def view_entries():
    """View all journal entries."""
    if not os.path.exists(JOURNAL_FILE) or os.stat(JOURNAL_FILE).st_size == 0:
        print("\nNo journal entries found.")
        return

    print("\n=== All Journal Entries ===")
    with open(JOURNAL_FILE, "r") as file:
        for line in file:
            print(line.strip())


def search_entries():
    """Search for a specific journal entry."""
    keyword = input("\nEnter a keyword to search: ")
    found = False

    if not os.path.exists(JOURNAL_FILE) or os.stat(JOURNAL_FILE).st_size == 0:
        print("No journal entries to search.")
        return

    print("\n=== Search Results ===")
    with open(JOURNAL_FILE, "r") as file:
        for line in file:
            if keyword.lower() in line.lower():
                print(line.strip())
                found = True

    if not found:
        print(f"No entries found containing '{keyword}'.")


def main():
    while True:
        display_menu()
        choice = input("\nChoose an option (1-4): ")

        if choice == "1":
            write_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            search_entries()
        elif choice == "4":
            print("Exiting the journal app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
