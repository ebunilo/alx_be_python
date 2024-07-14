class Book:
    """Book class"""

    def __init__(self, title, author):
        """Initialize Book class

        Args:
            title (str): Title of the book
            author (str): Author of the book
        """
        self.title = title
        self.author = author
        self.__is_checked_out = False

    def is_checked_out(self):
        """Check if a book is checked out"""
        return self.__is_checked_out

    def check_out(self):
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
        """Initialize Library class"""
        self._books = []

    def add_book(self, book):
        """Add a book to the library"""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book from the library"""
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return None

    def return_book(self, title):
        """Return a book to the library"""
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return None

    def list_available_books(self):
        """Display available books in the library"""
        available_books = [
            book for book in self._books if not book.is_checked_out()]
        for book in available_books:
            print(f'{book.title} by {book.author}')
