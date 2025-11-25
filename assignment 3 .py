# Task 1: Book Class
class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {self.status}"

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status
        }

    def issue(self):
        if self.status == "available":
            self.status = "issued"
            print("Book issued successfully.")
        else:
            print("Book already issued.")

    def return_book(self):
        if self.status == "issued":
            self.status = "available"
            print("Book returned successfully.")
        else:
            print("Book was not issued.")


# Task 2: Library Inventory Class
class LibraryInventory:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added!")

    def search_by_title(self, title):
        for book in self.books:
            if book.title == title:
                print(book)
                return
        print("Book not found.")

    def search_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                print(book)
                return
        print("Book not found.")

    def display_all(self):
        if not self.books:
            print("No books found.")
        for book in self.books:
            print(book)

    def save_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                for book in self.books:
                    file.write(f"{book.title},{book.author},{book.isbn},{book.status}\n")
            print("Saved successfully.")
        except Exception as e:
            print(f"Error saving: {e}")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    title, author, isbn, status = line.strip().split(',')
                    loaded_book = Book(title, author, isbn, status)
                    self.books.append(loaded_book)
            print("Loaded successfully.")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"Error loading: {e}")


# Task 4: CLI
def interactive_cli():
    inventory = LibraryInventory()
    
    while True:
        print("\nMenu:")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book by Title")
        print("6. Search Book by ISBN")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            book = Book(title, author, isbn)
            inventory.add_book(book)

        elif choice == "2":
            isbn = input("Enter ISBN to issue: ")
            inventory.search_by_isbn(isbn)
            for b in inventory.books:
                if b.isbn == isbn:
                    b.issue()

        elif choice == "3":
            isbn = input("Enter ISBN to return: ")
            for b in inventory.books:
                if b.isbn == isbn:
                    b.return_book()

        elif choice == "4":
            inventory.display_all()

        elif choice == "5":
            title = input("Enter title: ")
            inventory.search_by_title(title)

        elif choice == "6":
            isbn = input("Enter ISBN: ")
            inventory.search_by_isbn(isbn)

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


# Task 5: Logging
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def log_example():
    try:
        logging.info("Program started.")
        1 / 0
    except ZeroDivisionError as e:
        logging.error(f"Error: {e}")
    finally:
        logging.info("Execution finished.")


# Run program
if __name__ == "__main__":
    interactive_cli()
    log_example()
