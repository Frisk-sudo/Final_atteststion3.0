import json
from collections import deque

class Book ():
    def __init__(self, title, author, pages, genre):
        self.__title = title
        self.__author = author
        self.__pages = pages
        self.__genre = genre

    # Геттеры
    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def pages(self):
        return self.__pages

    @property
    def genre(self):
        return self.__genre

    def get_information(self):
        return self.__title, self.__author, self.__pages, self.__genre
    
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
        self.__genre = genre.lower()

    def apply(self, books):
        result = []
        for book in books:
            if book.genre.lower() == self.genre:
                result.append(book)
        return result

# Наследование от BookFilter
class PagesFilter(BookFilter):
    def __init__(self, max_pages):
        self.__max_pages = max_pages

    def apply(self, books):
        result = []
        for book in books:
            if book.pages <= self.max_pages:
                result.append(book)
        return result

class BookManager:
    def __init__(self, data_file="books.json"):
        self.__data_file = data_file
        self.__books = []
        self.__history = deque(maxlen=10)
        self.__load_books()

    def add_book(self, book):
        if self.find_book_by_title(book.title):
            return False
        self.__books.append(book)
        self.__history.append("Добавлена книга: " + book.title)
        self.__save_books()
        return True

    def delete_book(self, title):
        book = self.find_book_by_title(title)
        if not book:
            return False
        self.__books.remove(book)
        self.__history.append("Удалена книга: " + title)
        self.__save_books()
        return True

    def find_book_by_title(self, title):
        for book in self.__books:
            if book.title.lower() == title.lower():
                return book
        return None

    def get_all_books(self):
        return self.__books

    def get_history(self):
        return list(self.__history)

    def filter_by_genre(self, genre):
        filter_obj = GenreFilter(genre)
        return filter_obj.apply(self.__books)

    def filter_by_pages(self, max_pages):
        filter_obj = PagesFilter(max_pages)
        return filter_obj.apply(self.__books)

    def __save_books(self):
        with open(self.__data_file, 'w', encoding='utf-8') as f:
            json.dump([book.to_dict() for book in self.__books], f, indent=2)

    def __load_books(self):
        try:
            with open(self.__data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.__books = [Book.from_dict(item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.__books = []