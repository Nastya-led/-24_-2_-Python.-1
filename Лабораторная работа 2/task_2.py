BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    """
    Класс, представляющий книгу.
    """

    def __init__(self, id_: int, name: str, pages: int) -> None:
        """
        Инициализация книги.

        :param id_: Идентификатор книги.
        :param name: Название книги.
        :param pages: Количество страниц, должно быть положительным.
        """
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным.")

        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        Возвращает строковое представление книги.

        :return: Строка формата 'Книга "название_книги"'
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Возвращает строку, по которой можно создать аналогичный экземпляр.

        :return: Валидная Python-строка для инициализации объекта
        """
        return f"Book(id_={self.id}, name={repr(self.name)}, pages={self.pages})"


class Library:
    """
    Класс, представляющий библиотеку.
    """

    def __init__(self, books=None) -> None:
        """
        Инициализация библиотеки.

        :param books: Список книг (по умолчанию пустой список).
        """
        self.books = books if books is not None else []

    def get_next_book_id(self) -> int:
        """
        Возвращает идентификатор для добавления новой книги в библиотеку.

        :return: Следующий идентификатор (1, если библиотека пустая, иначе +1 к максимальному id).
        """
        if not self.books:
            return 1
        return max(book.id for book in self.books) + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Возвращает индекс книги в списке по её идентификатору.

        :param book_id: Идентификатор книги.
        :return: Индекс книги в списке.

        :raises ValueError: Если книги с таким id нет.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # Проверяем следующий id для пустой библиотеки (должно быть 1)

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # Инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # Проверяем следующий id для непустой библиотеки (должно быть 3)

    print(library_with_books.get_index_by_book_id(1))  # Проверяем индекс книги с id = 1 (должно быть 0)
