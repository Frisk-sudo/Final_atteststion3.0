import json
from collections import deque

class Book ():
    def __init__(self, title, auther, pages):
        self.__title = title
        self.__auther = auther
        self.__pages = pages

    def get_information (self):
        return self.__title, self.__auther, self.__pages
    
    def to_dict(self) -> dict:
        return {
            'title': self.title,
            'author': self.author,
            'genre': self.genre,
            'pages': self.pages
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Book':
        return cls(
            title=data['title'],
            author=data['author'],
            genre=data['genre'],
            pages=data['pages']
        )

class BookFilter:
    def apply(self, books):
        raise NotImplementedError("Subclasses must implement apply method")

# Наследование от BookFilter
class GenreFilter(BookFilter):
    def __init__(self, genre):
        self.genre = genre.lower()

    def apply(self, books):
        result = []
        for book in books:
            if book.genre.lower() == self.genre:
                result.append(book)
        return result

# Наследование от BookFilter
class PagesFilter(BookFilter):
    def __init__(self, max_pages):
        self.max_pages = max_pages

    def apply(self, books):
        result = []
        for book in books:
            if book.pages <= self.max_pages:
                result.append(book)
        return result

class BookManager:
    def __init__(self, data_file='data/books.json'):
        self.data_file = data_file
        self.books = []
        self.history = deque(maxlen=10)
        self.load_books()

    def add_book(self, book):
        if self.find_book_by_title(book.title):
            return False
        self.books.append(book)
        self.history.append("Добавлена книга: " + book.title)
        self.save_books()
        return True

    def save_books(self):
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump([book.to_dict() for book in self.books], f, indent=2)

    def load_books(self):
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.books = [Book.from_dict(item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []

    def delete_book(self, title):
        book = self.find_book_by_title(title)
        if not book:
            return False

        self.books.remove(book)
        self.history.append("Удалена книга: " + title)
        self.save_books()
        return True

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None