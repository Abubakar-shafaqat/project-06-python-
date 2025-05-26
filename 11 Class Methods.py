# Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def display_total_books(cls, message):
        print(message)
        print(f"Total Books: {cls.total_books}")

    # If you want to display instance information, use a regular method
    def display_book_info(self, message):
        print(message)
        print(f"\tTitle: {self.title}, Author: {self.author}")
        print(f"\tTotal Books: {Book.total_books}")
        
book1:Book = Book("To Kill a Mockingbird", "Harper Lee")
book1.display_book_info("\n1st Book Details :")
book2:Book = Book("1984", "George Orwell")
book2.display_book_info("\n2nd Book Details :")
book3:Book = Book("The Great Gatsby", "F. Scott Fitzgerald")
book3.display_book_info("\n3rd Book Details :")

