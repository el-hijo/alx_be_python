class Book:
    def __init__(self,title,author,_is_checked_out):
        self.title = title
        self.author = author
        self.__is_checked_out = False
    def check_out(self):
        if not self.__is_checked_out:
            print(f"'{self.title}' has been checked out.")
        else:
            print(f"'{self.title}' is already checked out.")
            
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not checked out.")
            
    def is_available(self):
        return not self._is_checked_out   
        
class Library:
    def __init__(self):
        self._books = []
        
    def add_book(self, book):
         self._books.append(book)
         print(f"Book '{book.title}' by {book.author} added to the library.")
        
    def check_out_book(self, title):
         for book in self._books:
             if book.title == title:
                 book.check_out()  
                 return
         print(f"No book found with title '{title}'.")     
     
    def list_available_books(self):
         available_books = [book for book in self.books if book.is_available()] 
         if available_books:
             print("\nAvailable books:")
             for book in available_books:
                 print(f"-{book.title} by {book.author}")
         else:
             print("\nNo books are currently available.")