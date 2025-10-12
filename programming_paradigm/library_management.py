# library_management.py

class Book:
    """Represents a single book in the library."""

    def __init__(self, title, author):
        self.title = title                 # public
        self.author = author               # public
        self._is_checked_out = False       # "private" by convention

    @property
    def is_checked_out(self):
        """Read-only view of checkout state."""
        return self._is_checked_out

    def check_out(self):
        """Mark the book as checked out; return True if successful."""
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_book(self):
        """Mark the book as returned; return True if successful."""
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True


class Library:
    """Manages a collection of Book instances."""

    def __init__(self):
        self._books = []  # private list of books

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def _find_by_title(self, title):
        """Internal helper to find a book by exact title match (case-sensitive)."""
        for book in self._books:
            if book.title == title:
                return book
        return None

    def check_out_book(self, title):
        """
        Check out a book by title.
        Returns True if the book existed and was successfully checked out.
        """
        book = self._find_by_title(title)
        if book is None:
            return False
        return book.check_out()

    def return_book(self, title):
        """
        Return a book by title.
        Returns True if the book existed and was successfully returned.
        """
        book = self._find_by_title(title)
        if book is None:
            return False
        return book.return_book()

    def list_available_books(self):
        """
        Print available (not checked out) books, one per line, in the format:
        <Title> by <Author>
        """
        for book in self._books:
            if not book.is_checked_out:
                print(f"{book.title} by {book.author}")
