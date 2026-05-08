"""
Простые тесты для системы управления книгами.
"""

import sys
import os
import json
from collections import deque

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models import Book, BookManager, GenreFilter, PagesFilter

def test_book_creation():
    """Тест создания книги."""
    try:
        book = Book("Война и мир", "Лев Толстой", 1225, "Роман")
        assert book.title == "Война и мир"
        assert book.author == "Лев Толстой"
        assert book.pages == 1225
        assert book.genre == "Роман"
        print("✅ Тест 1 (создание книги): пройден")
        return True
    except Exception as e:
        print(f"❌ Тест 1 (создание книги): ошибка - {e}")
        return False

def test_add_and_find_book():
    """Тест добавления и поиска книги."""
    try:
        manager = BookManager(data_file="test_books.json")
        book = Book("1984", "Джордж Оруэлл", 328, "Антиутопия")
        manager.add_book(book)
        
        found_book = manager.find_book_by_title("1984")
        assert found_book is not None
        assert found_book.title == "1984"
        print("✅ Тест 2 (добавление и поиск книги): пройден")
        return True
    except Exception as e:
        print(f"❌ Тест 2 (добавление и поиск книги): ошибка - {e}")
        return False

def test_delete_book():
    """Тест удаления книги."""
    try:
        manager = BookManager(data_file="test_books.json")
        book = Book("Мастер и Маргарита", "Михаил Булгаков", 480, "Роман")
        manager.add_book(book)
        
        deleted = manager.delete_book("Мастер и Маргарита")
        assert deleted is True
        found_book = manager.find_book_by_title("Мастер и Маргарита")
        assert found_book is None
        print("✅ Тест 3 (удаление книги): пройден")
        return True
    except Exception as e:
        print(f"❌ Тест 3 (удаление книги): ошибка - {e}")
        return False

def test_filter_by_genre():
    """Тест фильтрации книг по жанру."""
    try:
        manager = BookManager(data_file="test_books.json")
        book1 = Book("Гарри Поттер", "Джоан Роулинг", 435, "Фэнтези")
        book2 = Book("Убить пересмешника", "Харпер Ли", 376, "Роман")
        manager.add_book(book1)
        manager.add_book(book2)
        
        filtered_books = manager.filter_by_genre("Фэнтези")
        assert len(filtered_books) == 1
        assert filtered_books[0].title == "Гарри Поттер"
        print("✅ Тест 4 (фильтрация по жанру): пройден")
        return True
    except Exception as e:
        print(f"❌ Тест 4 (фильтрация по жанру): ошибка - {e}")
        return False

def test_filter_by_pages():
    """Тест фильтрации книг по количеству страниц."""
    try:
        manager = BookManager(data_file="test_books.json")
        book1 = Book("Маленький принц", "Антуан де Сент-Экзюпери", 96, "Сказка")
        book2 = Book("Война и мир", "Лев Толстой", 1225, "Роман")
        manager.add_book(book1)
        manager.add_book(book2)
        
        filtered_books = manager.filter_by_pages(100)
        assert len(filtered_books) == 1
        assert filtered_books[0].title == "Маленький принц"
        print("✅ Тест 5 (фильтрация по страницам): пройден")
        return True
    except Exception as e:
        print(f"❌ Тест 5 (фильтрация по страницам): ошибка - {e}")
        return False

def test_history():
    """Тест истории операций."""
    try:
        manager = BookManager(data_file="test_books.json")
        book = Book("451° по Фаренгейту", "Рэй Брэдбери", 256, "Антиутопия")
        manager.add_book(book)
        manager.delete_book("451° по Фаренгейту")
        
        history = manager.get_history()
        assert len(history) >= 2
        assert "Добавлена книга" in history[0]
        assert "Удалена книга" in history[1]
        print("✅ Тест 6 (история операций): пройден")
        return True
    except Exception as e:
        print(f"❌ Тест 6 (история операций): ошибка - {e}")
        return False

def run_all_tests():
    """Запуск всех тестов."""
    print("\n" + "="*40)
    print("🧪 ЗАПУСК ТЕСТОВ СИСТЕМЫ УПРАВЛЕНИЯ КНИГАМИ")
    print("="*40 + "\n")
    
    tests = [
        test_book_creation,
        test_add_and_find_book,
        test_delete_book,
        test_filter_by_genre,
        test_filter_by_pages,
        test_history
    ]
    
    passed = 0
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("="*40)
    print(f"📊 РЕЗУЛЬТАТ: {passed}/{len(tests)} тестов пройдено")
    
    if passed == len(tests):
        print("✅ ВСЕ ТЕСТЫ ПРОЙДЕНЫ!")
        print("="*40 + "\n")
        return True
    else:
        print(f"❌ НЕ ПРОЙДЕНО {len(tests) - passed} тестов")
        print("="*40 + "\n")
        return False

if __name__ == "__main__":
    run_all_tests()