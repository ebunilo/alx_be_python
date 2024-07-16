class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author


class EBook(Book):
    def __init__(self, title: str, author: str, filesize: int):
        super().__init__(title, author)
        self.filesize = filesize


class PrintBook(Book):
    def __init__(self, title: str, author: str, pagecount: int):
        super().__init__(title, author)
        self.pagecount = pagecount


class Library:
    def __init__(self):
        self.book = []

    def add_book(self, book):
        return self.book.append(book)

    def list_books(self):
        for book in self.book:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.filesize}")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.pagecount}")
            else:
                print(f"Book: {book.title} by {book.author}")
