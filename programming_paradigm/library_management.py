class Book:
    """Book class"""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False

    def is_checked_out(self):
        """Check if a book is checked out"""
        return self.__is_checked_out

    def check_out(self):
        """Check out a book"""
        if not self.__is_checked_out:
            self.__is_checked_out = True
            return True
        return False

    def return_book(self):
        if self.__is_checked_out:
            self.__is_checked_out = False
            return True
        return False


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
                book.check_out()

    def return_book(self, title):
        for book in self.__books:
            if book.title == title:
                return book.return_book()
        return False

    def list_available_books(self):
        """Display available books in the library"""
        available_books = [
            book for book in self.__books if not book.is_checked_out()]
        for book in available_books:
            print(f'{book.title} by {book.author}')

    def all_books(self):
        """Display all books in the library"""
        for book in self.__books:
            print(f'{book.title} by {book.author}, {book.is_checked_out()=}')


# book1 = Book("The Fury", "Dan Brown")
# book2 = Book("Lost Kingdom", "Kevin Hart")
# book3 = Book("The last day", "Robert Langston")

# library = Library()
# library.add_book(Book("Brave New World", "Aldous Huxley"))
# library.add_book(Book("1984", "George Orwell"))
