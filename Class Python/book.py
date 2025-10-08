class Book:
    def __init__(self, title, author, pages, price):
        
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
    


#Create instance of Book
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180, 10.99)
book2 = Book("1984", "George Orwell", 328, 8.99)
book3 = Book("To Kill a Mockingbird", "Harper Lee", 281, 7.99)
book4 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 223, 12.99)


#print book details
print(f"Title: {book1.title}, Author: {book1.author}, Pages: {book1.pages}, Price: ${book1.price:.2f}")
print(f"Title: {book2.title}, Author: {book2.author}, Pages: {book2.pages}, Price: ${book2.price:.2f}")
print(book1.price + book2.price + book3.price  + book4.price)
print(book4.title)

