import pytest


@pytest.fixture
def clear_books_database():
    print("[FIXTURE] Удаляем все данные из БД")


@pytest.fixture
def fill_books_database():
    print("[FIXTURE] Создаём новые данные из БД")


@pytest.mark.usefixtures('fill_books_database', 'clear_books_database')
class TestLibrary:

    def test_read_book_from_library(self):
        ...

    def test_delete_book_from_library(self):
        ...

