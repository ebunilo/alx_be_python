class Book:
    """ A Book class that implements both __str__ and __repr__ magic methods to provide
    different string representations of the Book object."""
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r}, pages={self.pages!r})"

    def __str__(self):
        return f"{self.title!r} was written by {self.author!r} and has {self.pages!r} pages"


book = Book("A New Dawn", "Achebe", "200")
print(repr(book))
print(str(book))
