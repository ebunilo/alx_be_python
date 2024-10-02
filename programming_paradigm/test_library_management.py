import unittest
from library_management import Book, Library

class TestBook(unittest.TestCase):
    def setUp(self):
        """Create a sample book to use in tests."""
        self.book = Book("The Great Gatsby", "F. Scott Fitzgerald")

    def test_initialization(self):
        """Test if a book is initialized correctly."""
        self.assertEqual(self.book.title, "The Great Gatsby")
        self.assertEqual(self.book.author, "F. Scott Fitzgerald")
        self.assertFalse(self.book._is_checked_out)

    def test_str_representation(self):
        """Test the string representation of the book."""
        self.assertEqual(str(self.book), "The Great Gatsby by F. Scott Fitzgerald")

    def test_check_out_success(self):
        """Test successful book check out."""
        result = self.book.check_out()
        self.assertTrue(result)
        self.assertTrue(self.book._is_checked_out)

    def test_check_out_failure(self):
        """Test failing to check out a book that's already checked out."""
        self.book.check_out()  # First checkout
        result = self.book.check_out()  # Second checkout attempt
        self.assertFalse(result)

    def test_return_success(self):
        """Test successful book return."""
        self.book.check_out()  # First checkout
        result = self.book.return_book()
        self.assertTrue(result)
        self.assertFalse(self.book._is_checked_out)

    def test_return_failure(self):
        """Test failing to return a book that isn't checked out."""
        result = self.book.return_book()
        self.assertFalse(result)


class TestLibrary(unittest.TestCase):
    def setUp(self):
        """Create a library and some books to use in tests."""
        self.library = Library()
        self.book1 = Book("1984", "George Orwell")
        self.book2 = Book("To Kill a Mockingbird", "Harper Lee")
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)

    def test_add_book(self):
        """Test that books can be added to the library."""
        self.assertEqual(len(self.library._books), 2)
        self.assertIn(self.book1, self.library._books)
        self.assertIn(self.book2, self.library._books)

    def test_check_out_book_success(self):
        """Test successful checkout of a book by title."""
        result = self.library.check_out_book("1984")
        self.assertTrue(result)
        self.assertTrue(self.book1._is_checked_out)

    def test_check_out_book_failure(self):
        """Test trying to check out a non-existent book."""
        result = self.library.check_out_book("Non-Existent Book")
        self.assertIsNone(result)

    def test_return_book_success(self):
        """Test successful return of a checked-out book."""
        self.library.check_out_book("1984")
        result = self.library.return_book("1984")
        self.assertTrue(result)
        self.assertFalse(self.book1._is_checked_out)

    def test_return_book_failure(self):
        """Test trying to return a book that's not checked out."""
        result = self.library.return_book("1984")
        self.assertFalse(result)

    # def test_list_available_books(self):
    #     """Test listing available books (those not checked out)."""
    #     with self.assertLogs() as log:
    #         self.library.list_available_books()
    #         self.assertIn("1984 by George Orwell", log.output[0])
    #         self.assertIn("To Kill a Mockingbird by Harper Lee", log.output[1])


if __name__ == '__main__':
    unittest.main()
