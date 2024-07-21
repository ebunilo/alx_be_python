class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title: str, author: str, filesize: int):
        super().__init__(title, author)
        self.filesize = filesize

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.filesize}"


class PrintBook(Book):
    def __init__(self, title: str, author: str, pagecount: int):
        super().__init__(title, author)
        self.pagecount = pagecount

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.pagecount}"


class Library:
    def __init__(self):
        self.book = []

    def add_book(self, book):
        return self.book.append(book)

    def list_books(self):
        for book in self.book:
            if isinstance(book, EBook):
                print(book)
            elif isinstance(book, PrintBook):
                print(book)
            else:
                print(book)
