class View:
    @staticmethod
    def show_menu():
        print("\n=== Book Tracker ===")
        print("Выберите действие:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Посмотреть все книги")
        print("4. Отсортировать по жанру")
        print("5. Отсортировать по количеству страниц")
        print("6. Посмотреть историю")
        print("7. Выход")

    @staticmethod
    def get_user_choice():
        return input("\nВведите свой выбор (1-7): ").strip()

    @staticmethod
    def show_books(books):
        if not books:
            print("Книги не найдены")
            return
        print("\nКниги:")
        for i, book in enumerate(books, 1):
            print(f"{i}. Название: {book.title} | Автор {book.author} | Жанр: {book.genre} | Количесво страниц: {book.pages}")

    @staticmethod
    def show_history(history):
        if not history:
            print("Истории нет")
            return
        print("\nИстория:")
        for i, action in enumerate(history, 1):
            print(f"{i}. {action}")

    @staticmethod
    def get_book_input():
        title = input("Введите название: ").strip()
        author = input("Введите автора: ").strip()
        genre = input("Введите жанр: ").strip()
        pages = input("Введите количество страниц: ").strip()
        return {"title": title, "author": author, "genre": genre, "pages": pages}

    @staticmethod
    def get_search_input():
        return input("Введите поисковый запрос ").strip()

    @staticmethod
    def get_pages_input():
        while True:
            try:
                pages = int(input("Введите максимальное число страниц: "))
                return pages
            except ValueError:
                print("Введите число!")

    @staticmethod
    def show_message(message):
        print(f"\n{message}")
