class Book:
    """
    A base class to represent a book.

    Attributes:
    -----------
    title : str
        The title of the book.
    author : str
        The author of the book.
    """

    def __init__(self, title: str, author: str):
        """
        Initializes a new Book instance.

        Parameters:
        -----------
        title : str
            The title of the book.
        author : str
            The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Returns a string representation of the Book instance.

        Returns:
        --------
        str
            A string in the format "Book: {title} by {author}".
        """
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """
    A class to represent an electronic book, inheriting from the Book class.

    Attributes:
    -----------
    file_size : int
        The file size of the eBook in kilobytes.
    """

    def __init__(self, title: str, author: str, file_size: int):
        """
        Initializes a new EBook instance.

        Parameters:
        -----------
        title : str
            The title of the eBook.
        author : str
            The author of the eBook.
        file_size : int
            The file size of the eBook in kilobytes.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """
        Returns a string representation of the EBook instance.

        Returns:
        --------
        str
            A string in the format "EBook: {title} by {author}, File Size: {file_size}KB".
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    A class to represent a printed book, inheriting from the Book class.

    Attributes:
    -----------
    page_count : int
        The number of pages in the printed book.
    """

    def __init__(self, title: str, author: str, page_count: int):
        """
        Initializes a new PrintBook instance.

        Parameters:
        -----------
        title : str
            The title of the printed book.
        author : str
            The author of the printed book.
        page_count : int
            The number of pages in the printed book.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """
        Returns a string representation of the PrintBook instance.

        Returns:
        --------
        str
            A string in the format "PrintBook: {title} by {author}, Page Count: {page_count}".
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """
    A class to represent a library, containing a collection of books.

    Attributes:
    -----------
    books : list
        A list to store the books in the library.
    """

    def __init__(self):
        """
        Initializes a new Library instance.
        """
        self.books = []

    def add_book(self, book: object):
        """
        Adds a book to the library's collection.

        Parameters:
        -----------
        book : Book
            An instance of the Book class or its subclasses (EBook, PrintBook).
        """
        return self.books.append(book)

    def list_books(self):
        """
        Prints out the details of all books in the library's collection.
        """
        for book in self.books:
            print(book)
