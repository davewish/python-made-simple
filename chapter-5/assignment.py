# Base class for library items
class LibraryItem:
    def __init__(self, title):
        self.title = title
        self.is_available = True

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Available: {'Yes' if self.is_available else 'No'}")

# Derived class for books
class Book(LibraryItem):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author

    def display_details(self):
        super().display_details()
        print(f"Author: {self.author}")

# Library class to manage books
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Book '{title}' removed from the library.")
                return
        print(f"Book '{title}' not found.")

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                book.display_details()
                return
        print(f"Book '{title}' not found.")

    def display_books(self):
        if self.books:
            print("Available books:")
            for book in self.books:
                if book.is_available:
                    book.display_details()
        else:
            print("No books available.")

# User class to manage borrowing and returning books
class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, library, title):
        for book in library.books:
            if book.title == title and book.is_available:
                book.is_available = False
                self.borrowed_books.append(book)
                print(f"Book '{title}' borrowed by {self.name}.")
                return
        print(f"Book '{title}' is not available.")

    def return_book(self, library, title):
        for book in self.borrowed_books:
            if book.title == title:
                book.is_available = True
                self.borrowed_books.remove(book)
                print(f"Book '{title}' returned by {self.name}.")
                return
        print(f"Book '{title}' not found in your borrowed list.")

# Main program loop
def main():
    library = Library()
    user = User("Alice")

    while True:
        print("\nLibrary Management System Menu:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Display Available Books")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            book = Book(title, author)
            library.add_book(book)
        elif choice == "2":
            title = input("Enter the book title to remove: ")
            library.remove_book(title)
        elif choice == "3":
            title = input("Enter the book title to search: ")
            library.search_book(title)
        elif choice == "4":
            title = input("Enter the book title to borrow: ")
            user.borrow_book(library, title)
        elif choice == "5":
            title = input("Enter the book title to return: ")
            user.return_book(library, title)
        elif choice == "6":
            library.display_books()
        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()