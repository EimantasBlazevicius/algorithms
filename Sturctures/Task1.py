from typing import List


class BooksStack:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.books = []

    def __add__(self, second_stack):
        new_stack = BooksStack(self.name, self.category)
        books_to_add = self.books + second_stack.books
        for book in books_to_add:
            new_stack.add_new_book(book)
        return new_stack

    # comparision
    def __gt__(self, second_stack):
        return len(self.books) > len(second_stack.books)

    def __lt__(self, second_stack):
        return len(self.books) < len(second_stack.books)

    def __ge__(self, second_stack):
        return len(self.books) >= len(second_stack.books)

    def __le__(self, second_stack):
        return len(self.books) <= len(second_stack.books)

    def __str__(self):
        return f"Stack: {self.name} with category of books: {self.category}"

    def __repr__(self):
        return f"stack_name: {self.name}"

    def __len__(self):
        return len(self.books)

    def add_new_book(self, title: str):
        self.books.append(title)

    def get_book(self):
        return self.books.pop()

    def all_books(self) -> List[str]:
        return self.books


my_books = BooksStack("My Stack of Books", "Natural")

my_books.add_new_book("Cheetahs")
my_books.add_new_book("Elephants")
my_books.add_new_book("Cats")

print(my_books.all_books())
print(my_books.get_book())
print(my_books.all_books())

her_books = BooksStack("Her Stack of Books", "Natural")
her_books.add_new_book("Horses")

my_books = my_books + her_books
print(my_books.all_books())

print(my_books > her_books)
print(my_books <= her_books)

print(my_books)
print(repr(my_books))

print(len(my_books))
