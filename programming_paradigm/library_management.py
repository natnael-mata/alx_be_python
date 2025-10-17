class Book:
    
    def __init__(self, title, author, is_checked_out=False):
        self.title = title
        self.author = author
        self._is_checked_out = is_checked_out

    def checkout(self):
        if self._is_checked_out == False:
            self._is_checked_out = True
            return True
        else:
            return False
        
    def return_book(self):
        if self._is_checked_out == True:
            self._is_checked_out = False
            return True
        else: 
            return False

class Library:
    
    def __init__(self):
        self._books = []
    
    def add_book(self, title, author):
        new_book = Book(title, author)
        self._books.append(new_book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out == False:
                book.checkout()
                return f'{book.title} by {book.author}'  # Return the book info
            else:
                return "Book not available"

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out == True:
                    book.return_book()
            else:
                return None

    def list_available_books(self):
        available_books = [
            f'{book.title} by {book.author}' for book in self._books if not book._is_checked_out
        ]
        if available_books:
            return available_books
        return "No books available"




