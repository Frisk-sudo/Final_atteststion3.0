from models import Book, BookManager
from view import View

class Controller:
    def __init__(self):
        self.book_manager = BookManager()
        self.view = View()

    def run(self):
        while True:
            self.view.show_menu()
            choice = self.view.get_user_choice()

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.remove_book()
            elif choice == '3':
                self.view_books()
            elif choice == '4':
                self.filter_by_genre()
            elif choice == '5':
                self.filter_by_pages()
            elif choice == '6':
                self.show_history()
            elif choice == '7':
                self.view.show_message("До свидания!")
                break
            else:
                self.view.show_message("Ошибка ввода. Введите число от 1 до 7!")

    def add_book(self):
        try:
            book_data = self.view.get_book_input()
            pages = int(book_data["pages"])
            book = Book(book_data["title"], book_data["author"], pages, book_data["genre"])
            if self.book_manager.add_book(book):
                self.view.show_message(f"Книга '{book.title}' успешно добавлена!")
            else:
                self.view.show_message(f"Книга с названием '{book.title}' уже существует!")
        except ValueError:
            self.view.show_message("Ошибка: количество страниц должно быть числом!")

    def remove_book(self):
        title = self.view.get_search_input()
        if self.book_manager.delete_book(title):
            self.view.show_message(f"Книга '{title}' успешно удалена!")
        else:
            self.view.show_message(f"Книга '{title}' не найдена!")

    def view_books(self):
        books = self.book_manager.get_all_books()
        self.view.show_books(books)

    def filter_by_genre(self):
        genre = self.view.get_search_input()
        filtered_books = self.book_manager.filter_by_genre(genre)
        self.view.show_books(filtered_books)

    def filter_by_pages(self):
        max_pages = self.view.get_pages_input()
        filtered_books = self.book_manager.filter_by_pages(max_pages)
        self.view.show_books(filtered_books)

    def show_history(self):
        history = self.book_manager.get_history()
        self.view.show_history(history)