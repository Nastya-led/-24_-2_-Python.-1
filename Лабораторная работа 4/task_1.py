from abc import ABC, abstractmethod


class ElectronicDevice(ABC):
    """
    Базовый класс для электронных устройств.
    """

    def __init__(self, brand: str, model: str, battery_life: float) -> None:
        """
        Инициализация электронного устройства.

        :param brand: Бренд устройства.
        :param model: Модель устройства.
        :param battery_life: Время автономной работы в часах, должно быть положительным числом.
        """
        if battery_life <= 0:
            raise ValueError("Время автономной работы должно быть положительным числом.")

        self._brand = brand  # Инкапсуляция: бренд нельзя изменять после инициализации
        self._model = model  # Инкапсуляция: модель нельзя изменять после инициализации
        self.battery_life = battery_life  # Время работы можно изменять

    @property
    def brand(self) -> str:
        """Возвращает бренд устройства (нельзя изменять)."""
        return self._brand

    @property
    def model(self) -> str:
        """Возвращает модель устройства (нельзя изменять)."""
        return self._model

    @abstractmethod
    def power_on(self) -> None:
        """Абстрактный метод для включения устройства."""
        pass

    def __str__(self) -> str:
        """Возвращает строковое представление устройства."""
        return f"{self.__class__.__name__}: {self.brand} {self.model}, автономность {self.battery_life} ч."

    def __repr__(self) -> str:
        """Возвращает строку для создания объекта."""
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, battery_life={self.battery_life})"


class Smartphone(ElectronicDevice):
    """
    Дочерний класс для смартфонов.
    """

    def __init__(self, brand: str, model: str, battery_life: float, sim_count: int) -> None:
        """
        Инициализация смартфона.

        :param brand: Бренд смартфона.
        :param model: Модель смартфона.
        :param battery_life: Время автономной работы (часы).
        :param sim_count: Количество SIM-карт (должно быть минимум 1).
        """
        super().__init__(brand, model, battery_life)

        if sim_count < 1:
            raise ValueError("Смартфон должен поддерживать хотя бы одну SIM-карту.")

        self.sim_count = sim_count  # Можно изменять

    def power_on(self) -> None:
        """Метод для включения смартфона."""
        print(f"Смартфон {self.brand} {self.model} включается...")

    def __str__(self) -> str:
        """Перегрузка метода __str__ для добавления информации о SIM-картах."""
        return super().__str__() + f", SIM-карт: {self.sim_count}"

    def make_call(self, number: str) -> None:
        """
        Метод для совершения звонка.

        :param number: Номер телефона.
        """
        print(f"Звонок на {number} с {self.brand} {self.model}...")


class Laptop(ElectronicDevice):
    """
    Дочерний класс для ноутбуков.
    """

    def __init__(self, brand: str, model: str, battery_life: float, ram: int) -> None:
        """
        Инициализация ноутбука.

        :param brand: Бренд ноутбука.
        :param model: Модель ноутбука.
        :param battery_life: Время автономной работы (часы).
        :param ram: Объем оперативной памяти в ГБ.
        """
        super().__init__(brand, model, battery_life)

        if ram <= 0:
            raise ValueError("Оперативная память должна быть больше 0 ГБ.")

        self.ram = ram  # Можно изменять

    def power_on(self) -> None:
        """Метод для включения ноутбука."""
        print(f"Ноутбук {self.brand} {self.model} загружается...")

    def __str__(self) -> str:
        """Перегрузка метода __str__ для добавления информации об ОЗУ."""
        return super().__str__() + f", ОЗУ: {self.ram} ГБ"

    def run_program(self, program_name: str) -> None:
        """
        Метод для запуска программы.

        :param program_name: Название программы.
        """
        print(f"Запуск {program_name} на {self.brand} {self.model}...")


if __name__ == "__main__":
    # Создание объектов
    phone = Smartphone("Apple", "iPhone 13", 20, 1)
    laptop = Laptop("Dell", "XPS 15", 10, 16)

    # Проверка методов
    print(phone)  # Смартфон
    print(laptop)  # Ноутбук

    print(repr(phone))
    print(repr(laptop))

    phone.power_on()
    laptop.power_on()

    phone.make_call("+123456789")
    laptop.run_program("PyCharm")
