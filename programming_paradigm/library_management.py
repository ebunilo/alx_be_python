class Book:
    """
    Represents a book in the library with a title, author, and a status indicating if it's checked out.

    :ivar title: The title of the book.
    :ivar author: The author of the book.
    :ivar _is_checked_out: Private attribute indicating if the book is currently checked out.
    """
    def __init__(self, title: str, author: str):
        """
        Initializes a new Book object with the provided title and author.

        :param title: The title of the book.
        :type title: str
        :param author: The author of the book.
        :type author: str
        """
        self.title = title
        self.author = author
        self._is_checked_out = False

    def __str__(self):
        """
        Returns a string representation of the book in the format 'title by author'.
        
        Returns:
            str: A string representing the book.
        """
        return f"{self.title} by {self.author}"

    def check_out(self):
        """
        Marks the book as checked out if it is not already checked out.

        :return: ``True`` if the book was successfully checked out, ``False`` otherwise.
        :rtype: bool
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """
        Marks the book as returned if it was previously checked out.

        :return: ``True`` if the book was successfully returned, ``False`` otherwise.
        :rtype: bool
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False


class Library:
    """
    Represents a collection of books and allows operations such as adding books, checking out books,
    returning books, and listing available books.

    :ivar _books: A private list containing the collection of books in the library.
    :vartype _books: list of Book
    """
    def __init__(self):
        """
        Initializes an empty library with an empty book collection.
        """
        self._books = []

    def add_book(self, book: str):
        """
        Adds a new book to the library's collection.

        :param book: The Book object to be added to the library.
        :type book: Book
        """
        self._books.append(book)

    def check_out_book(self, title: str):
        """
        Checks out a book from the library by its title.

        :param title: The title of the book to check out.
        :type title: str
        :return: ``True`` if the book was successfully checked out, ``False`` otherwise.
        :rtype: bool
        :raises None: If no book with the given title is found.
        """
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return None

    def return_book(self, title: str):
        """
        Returns a book to the library by its title.

        :param title: The title of the book to return.
        :type title: str
        :return: ``True`` if the book was successfully returned, ``False`` otherwise.
        :rtype: bool
        :raises None: If no book with the given title is found.
        """
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return None

    def list_available_books(self):
        """
        Prints a list of all available (not checked out) books in the library.
        """
        for book in self._books:
            if not book._is_checked_out:
                print(book)
