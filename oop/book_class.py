class Book:
    """
    A class to represent a book.

    Attributes:
    -----------
    title : str
        The title of the book.
    author : str
        The author of the book.
    year : int
        The year the book was published.
    """
    def __init__(self, title: str, author: str, year: int):
        """
        Initializes a new Book instance.

        Parameters:
        -----------
        title : str
            The title of the book.
        author : str
            The author of the book.
        year : int
            The year the book was published.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor method that prints a message when a Book object is deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Returns a string representation of the Book instance in a human-readable format.

        Returns:
        --------
        str
            A string in the format "{title} by {author}, published in {year}".
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns an unambiguous or official string representation of the Book instance, suitable for debugging.

        Returns:
        --------
        str
            A string in the format "Book('{title}', '{author}', {year})".
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
