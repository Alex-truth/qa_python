import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_with_invalid_name(self):
        collector = BooksCollector()
        collector.add_new_book('йцукенгшщзхъфывапролджэячсмитьбюйцукаипоеомвмвам')
        assert 'йцукенгшщзхъфывапролджэячсмитьбюйцукаипоеомвмвам' not in collector.books_genre

    def test_add_the_same_book(self):
        collector = BooksCollector()
        collector.add_new_book('Три мушкетёра')
        collector.add_new_book('Три мушкетёра')
        assert len(collector.get_books_genre()) == 1

@pytest.mark.parametrize("books, genre, expected_genre", [
    ("Дюна", "Фантастика", "Фантастика"),
    ("Пила", "Ужасы", "Ужасы"),
])
def test_set_book_genre(books, genre, expected_genre):
    books_collector = BooksCollector()
    books_collector.add_new_book(books)
    books_collector.set_book_genre(books, genre)
    assert books_collector.books_genre[books] == expected_genre

def test_get_book_genre():
    collector = BooksCollector()
    collector.add_new_book("Дюна")
    collector.set_book_genre("Дюна", "Фантастика")
    assert collector.get_book_genre("Дюна") == "Фантастика"



@pytest.mark.parametrize(
    "book1_genre, book2_genre, book3_genre, book4_genre, book5_genre, search_genre, expected_books", [
        ("Фантастика", "Ужасы", "Детективы", "Мультфильмы", "Комедии", "Фантастика", ["Book1"]),
        ("Фантастика", "Ужасы", "Детективы", "Мультфильмы", "Комедии", "Ужасы", ["Book2"]),
        ("Фантастика", "Ужасы", "Детективы", "Мультфильмы", "Комедии", "Детективы", ["Book3"]),
        ("Фантастика", "Ужасы", "Детективы", "Мультфильмы", "Комедии", "Мультфильмы", ["Book4"]),
        ("Фантастика", "Ужасы", "Детективы", "Мультфильмы", "Комедии", "Комедии", ["Book5"]),
    ])
def test_get_books_with_specific_genre(book1_genre, book2_genre, book3_genre, book4_genre, book5_genre, search_genre,expected_books):
    collector = BooksCollector()

    collector.add_new_book("Book1")
    collector.add_new_book("Book2")
    collector.add_new_book("Book3")
    collector.add_new_book("Book4")
    collector.add_new_book("Book5")

    collector.set_book_genre("Book1", book1_genre)
    collector.set_book_genre("Book2", book2_genre)
    collector.set_book_genre("Book3", book3_genre)
    collector.set_book_genre("Book4", book4_genre)
    collector.set_book_genre("Book5", book5_genre)

    books = collector.get_books_with_specific_genre(search_genre)

    assert books == expected_books


def test_get_books_genre():
    collector = BooksCollector()
    collector.add_new_book("Дюна")
    collector.add_new_book("Пила")

    collector.set_book_genre("Дюна", "Фантастика")
    collector.set_book_genre("Пила", "Ужасы")

    books_genre = collector.get_books_genre()
    assert books_genre == {"Дюна": "Фантастика", "Пила": "Ужасы"}


def test_get_books_for_children():
    collector = BooksCollector()
    collector.add_new_book("Колобок")
    collector.set_book_genre("Колобок", "Мультфильмы")
    books_for_children = collector.get_books_for_children()
    assert "Колобок" in books_for_children


def test_add_book_in_favorites():
    collector = BooksCollector()
    collector.add_new_book("Шерлок Холмс")
    collector.set_book_genre("Шерлок Холмс", "Детективы")
    collector.add_book_in_favorites("Шерлок Холмс")

    assert "Шерлок Холмс" in collector.favorites


def test_delete_book_from_favorites():
    collector = BooksCollector()
    collector.add_new_book("Шерлок Холмс")
    collector.set_book_genre("Шерлок Холмс", "Детективы")
    collector.add_book_in_favorites("Шерлок Холмс")
    collector.delete_book_from_favorites("Шерлок Холмс")
    assert "Шерлок Холмс" not in collector.favorites


def test_get_list_of_favorites_books():
    collector = BooksCollector()
    collector.add_new_book("Шерлок Холмс")
    collector.set_book_genre("Шерлок Холмс", "Детективы")
    collector.add_book_in_favorites("Шерлок Холмс")
    favorites = collector.get_list_of_favorites_books()
    assert favorites == ["Шерлок Холмс"]