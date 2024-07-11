class Book:
    """Book class"""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False

    def is_checked_out(self):
        """Check if a book is checked out"""
        return self.__is_checked_out

    def set_status(self, status):
        self.__is_checked_out = status


class Library:
    """Library class"""

    def __init__(self):
        self.__books = []

    def add_book(self, book):
        """Add a book to the library"""
        self.__books.append(book)

    def check_out_book(self, title):
        """Check out a book from the library"""
        for book in self.__books:
            if book.title == title:
                book.set_status(True)

    def return_book(self, title):
        """Return a book to the library"""
        for book in self.__books:
            if book.title == title:
                book.set_status(False)

    def list_available_books(self):
        """Display available books in the library"""
        available_books = [
            book for book in self.__books if not book.is_checked_out()]
        for book in available_books:
            print(f'{book.title} by {book.author}')
