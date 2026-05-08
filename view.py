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
            print("Книги, подходящие под запрос, не найдены")
            return
        print("\nКниги:")
        for i, book in enumerate(books, 1):
            print(f"{i}. Название: {book.title} | Автор: {book.author} | Жанр: {book.genre} | Количесво страниц: {book.pages}")

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
        while True:
            title = input("Введите название: ").strip()
            if not title:
                print("Ошибка: название книги не может быть пустым. Попробуйте снова.")
                continue

            author = input("Введите автора: ").strip()
            if not author:
                print("Ошибка: имя автора не может быть пустым. Попробуйте снова.")
                continue

            genre = input("Введите жанр: ").strip()
            if not genre:
                print("Ошибка: жанр не может быть пустым. Попробуйте снова.")
                continue

            pages = input("Введите количество страниц: ").strip()
            if not pages:
                print("Ошибка: количество страниц не может быть пустым. Попробуйте снова.")
                continue

            try:
                pages_int = int(pages)
                if pages_int <= 0:
                    print("Ошибка: количество страниц должно быть положительным числом. Попробуйте снова.")
                    continue
                return {"title": title, "author": author, "genre": genre, "pages": pages_int}
            except ValueError:
                print("Ошибка: количество страниц должно быть числом. Попробуйте снова.")

    @staticmethod
    def get_search_genre_input():
        return input("Введите жанр книги: ").strip()

    @staticmethod
    def get_search_input():
        return input("Введите название книги: ").strip()

    @staticmethod
    def get_pages_input():
        while True:
            try:
                pages = int(input("Введите максимальное число страниц: "))
                return pages
            except ValueError:
                print("Ошибка. Введите число!")

    @staticmethod
    def show_message(message):
        print(f"\n{message}")
