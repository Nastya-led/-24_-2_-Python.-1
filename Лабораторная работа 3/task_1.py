class Book:
    """Базовый класс книги."""

    def __init__(self, name: str, author: str) -> None:
        self._name = name  # Приватные атрибуты для предотвращения изменений
        self._author = author

    @property
    def name(self) -> str:
        """Возвращает название книги (нельзя изменять)."""
        return self._name

    @property
    def author(self) -> str:
        """Возвращает автора книги (нельзя изменять)."""
        return self._author

    def __str__(self) -> str:
        return f'Книга "{self.name}". Автор: {self.author}'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс для бумажной книги."""

    def __init__(self, name: str, author: str, pages: int) -> None:
        super().__init__(name, author)
        self._pages = None  # Инициализация перед проверкой
        self.pages = pages  # Проверка в сеттере

    @property
    def pages(self) -> int:
        """Возвращает количество страниц."""
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        """Устанавливает количество страниц с проверкой."""
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    """Класс для аудиокниги."""

    def __init__(self, name: str, author: str, duration: float) -> None:
        super().__init__(name, author)
        self._duration = None  # Инициализация перед проверкой
        self.duration = duration  # Проверка в сеттере

    @property
    def duration(self) -> float:
        """Возвращает продолжительность аудиокниги."""
        return self._duration

    @duration.setter
    def duration(self, value: float) -> None:
        """Устанавливает продолжительность аудиокниги с проверкой."""
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Продолжительность книги должна быть положительным числом.")
        self._duration = float(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"


if __name__ == "__main__":
    # Пример использования
    paper_book = PaperBook("1984", "Джордж Оруэлл", 328)
    audio_book = AudioBook("1984", "Джордж Оруэлл", 11.5)


