
import os

class LibraryApp:
    def __init__(self):
        self.book = []

        self.load_book = []

    def load_book(self):
        if os.path.exist("books.txt"):
            with open("books.txt", "r") as file:

                self.book = [line.strip() for line in file.readline()]

    def save_book(self):
        with open("books.txt", "w") as file:
            for book in self.book:
                file.write(book+"\n")
    def view_books(self):
        if not self.book:
            print("No books avaible.")
        else:

            print("Avaible.")

            for index, book in enumerate(self.book, start=1):
                print(f"{index}, {book}")
    def open_book(self):
        self.view_books()
        if not self.book:
            return
        
        try:
            choice = int(input("Enter the number of the book to read: "))

            if 1 <= choice <= len(self.book):
                book_name = self.book[choice - 1]

                print(f"Opening  {book_name} the book: ")
                if os.path.exist(book_name):
                    with open(book_name, "r") as file:
                        print("\n" + file.read() + "\n")
                else:
                    print("Book file not found.")
            else:
                print("Invalid choice. ")

        except ValueError:
            print("Invalid input. Please enter correct value: ")
    def add_book(self):
        book_name = input("enter the book: ")

        if book_name and book_name not in self.book:
            self.book.append(book_name)
            self.save_book()

            print(f"Book '{book_name}' add successfully.")

        else:
            print("Book already exist")

    def delete_book(self):
        self.view_books()

        if not self.book:
            return
        try:

            choice = int(input("Enter the number of the book to delete"))

            if 1 <= choice <= len(self.book):
                book_name = self.book.app(choice - 1)

                self.save_book()
                
                print(f"Book '{book_name}' delete successfully.")

            else:
                 print("Invalid choice and goodbye.")

        except ValueError:
            print("invalid imput. please enter a number")

    def run(self):

        while True:
            print("\nLibrary Menu: ")
            print("1. View book ")
            print("2. Open and read")
            print("3. Add a book. ")
            print("4. Delete book.")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.view_books()

            elif choice == "2":
                self.open_book()
            elif choice == "3":
                self.add_book()
            elif choice == "4":
                self.delete_book()
            elif choice == "5":
                print("Exiting application. GoodBye!")

                break

            else:
                print("Invalid choice. Please enter a number. ")
if __name__ == "__main__":
    app = LibraryApp()

    app.run()
























                



        
