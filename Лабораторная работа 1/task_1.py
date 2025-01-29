# TODO Написать 3 класса с документацией и аннотацией типов

from abc import ABC, abstractmethod

class Device(ABC):
    """
    Абстрактный класс, представляющий устройство.
    """

    def __init__(self, brand: str, model: str) -> None:
        """
        Инициализирует устройство с заданными брендом и моделью.

        :param brand: Бренд устройства.
        :param model: Модель устройства.
        """
        self.brand = brand
        self.model = model

    @abstractmethod
    def power_on(self) -> None:
        """
        Включает устройство.

        >>> device = Device("BrandX", "ModelY")
        >>> device.power_on()
        """
        ...

    @abstractmethod
    def power_off(self) -> None:
        """
        Выключает устройство.

        >>> device = Device("BrandX", "ModelY")
        >>> device.power_off()
        """
        ...


class MediaFile(ABC):
    """
    Абстрактный класс, представляющий медиафайл.
    """

    def __init__(self, filename: str, filesize: float) -> None:
        """
        Инициализирует медиафайл с заданными именем файла и размером.

        :param filename: Имя файла.
        :param filesize: Размер файла в мегабайтах, должен быть положительным.
        """
        if filesize <= 0:
            raise ValueError("Размер файла должен быть положительным.")
        self.filename = filename
        self.filesize = filesize

    @abstractmethod
    def play(self) -> None:
        """
        Воспроизводит медиафайл.

        >>> media = MediaFile("song.mp3", 5.0)
        >>> media.play()
        """
        ...

    @abstractmethod
    def stop(self) -> None:
        """
        Останавливает воспроизведение медиафайла.

        >>> media = MediaFile("song.mp3", 5.0)
        >>> media.stop()
        """
        ...


class Vehicle(ABC):
    """
    Абстрактный класс, представляющий транспортное средство.
    """

    def __init__(self, make: str, model: str, year: int) -> None:
        """
        Инициализирует транспортное средство с заданными производителем, моделью и годом выпуска.

        :param make: Производитель транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска, должен быть не ранее 1886 года.
        """
        if year < 1886:
            raise ValueError("Год выпуска не может быть ранее 1886 года.")
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def start_engine(self) -> None:
        """
        Запускает двигатель транспортного средства.

        >>> vehicle = Vehicle("Toyota", "Corolla", 2020)
        >>> vehicle.start_engine()
        """
        ...

    @abstractmethod
    def stop_engine(self) -> None:
        """
        Останавливает двигатель транспортного средства.

        >>> vehicle = Vehicle("Toyota", "Corolla", 2020)
        >>> vehicle.stop_engine()
        """
        ...

    @abstractmethod
    def drive(self, distance: float) -> None:
        """
        Управляет транспортным средством на заданное расстояние.

        :param distance: Расстояние в километрах, должно быть положительным.

        >>> vehicle = Vehicle("Toyota", "Corolla", 2020)
        >>> vehicle.drive(150.0)
        """
        ...

