from typing import List, Optional


class Book:
    def __init__(self, title: str, author: str, year: Optional[int] = None):
        self.title: str = title
        self.author: str = author
        self.year: Optional[int] = year

    def get_description(self) -> str:
        desc = f"'{self.title}' by {self.author}"
        if self.year:
            desc += f" (published in {self.year})"  # Type error if year is not int or None
        return desc


class Library:
    def __init__(self, name: str):
        self.name: str = name
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def find_book_by_title(self, title: str) -> Optional[Book]:
        for book in self.books:
            if book.title == title:  # Type error if book.title is not a string
                return book
        return None


# Intended type-correct usage
book1 = Book("1984", "George Orwell", 1949)

my_library = Library("Community Library")
my_library.add_book(book1)

# Scenario 1: Incorrect type for a Book attribute
book_with_wrong_year = Book(
    "Brave New World", "Aldous Huxley", "Nineteen Thirty-Two"
)  # Type Error: Expected Optional[int] for year, got str
my_library.add_book(book_with_wrong_year)


# Scenario 2: Incorrect type passed to a method
my_library.add_book("A string instead of a Book object")  # Type Error: Expected Book, got str


# Scenario 3: Incorrectly assuming the return type of a function
found_book_details: str = my_library.find_book_by_title("1984")  # Type Error: Expected str, got Optional[Book]
if found_book_details:
    print(found_book_details.upper())  # This would cause a runtime error if not caught by type checker,
    #  as Optional[Book] doesn't have .upper()

# To demonstrate a potential error within Book.get_description if year was not Optional[int]
book_bad_year = Book("Test Book", "Test Author")
book_bad_year.year = "A string year"  # This would be a type error if year was annotated as int, not Optional[int]
print(book_bad_year.get_description())  # And this would lead to issues

# Correct way to handle Optional return type
found_book_object = my_library.find_book_by_title("1984")
if found_book_object:
    print(f"Found: {found_book_object.get_description()}")
else:
    print("Book not found.")
