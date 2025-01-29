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

if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]

    for book in list_books:
        print(book)  # Проверяем метод __str__

    print(list_books)  # Проверяем метод __repr__
