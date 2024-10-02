class Book:
    """
    Represents a book in the library with a title, author, and a status indicating if it's checked out.
    
    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        _is_checked_out (bool): Private attribute indicating if the book is currently checked out.
    """
    def __init__(self, title: str, author: str):
        """
        Initializes a new Book object with the provided title and author.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
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
        
        Returns:
            bool: True if the book was successfully checked out, False otherwise.
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """
        Marks the book as returned if it was previously checked out.
        
        Returns:
            bool: True if the book was successfully returned, False otherwise.
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False


class Library:
    """
    Represents a collection of books and allows operations such as adding books, checking out books,
    returning books, and listing available books.
    
    Attributes:
        _books (list[Book]): A private list containing the collection of books in the library.
    """
    def __init__(self):
        """
        Initializes an empty library with an empty book collection.
        """
        self._books = []

    def add_book(self, book: str):
        """
        Adds a new book to the library's collection.
        
        Args:
            book (Book): The Book object to be added to the library.
        """
        self._books.append(book)

    def check_out_book(self, title: str):
        """
        Checks out a book from the library by its title.
        
        Args:
            title (str): The title of the book to check out.
        
        Returns:
            bool: True if the book was successfully checked out, False otherwise.
            None: If no book with the given title is found.
        """
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return None

    def return_book(self, title: str):
        """
        Returns a book to the library by its title.
        
        Args:
            title (str): The title of the book to return.
        
        Returns:
            bool: True if the book was successfully returned, False otherwise.
            None: If no book with the given title is found.
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
