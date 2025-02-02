class Book:
    """Базовый класс книги."""
    def __init__(self, name: str, author: str):
        self._name = name  # Внутреннее хранение атрибутов
        self._author = author

    @property
    def name(self):
        return self._name  # Геттер для name

    @property
    def author(self):
        return self._author  # Геттер для author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)  # Наследуем конструктор от Book
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int):
            raise ValueError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть больше нуля")
        self._pages = value

    def __str__(self):
        return f"Бумажная книга '{self.name}'. Автор {self.author}. Количество страниц: {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)  # Наследуем конструктор от Book
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, float):
            raise ValueError("Продолжительность книги должна быть числом с плавающей запятой")
        if value <= 0:
            raise ValueError("Продолжительность книги должна быть больше нуля")
        self._duration = value

    def __str__(self):
        return f"Аудиокнига '{self.name}'. Автор {self.author}. Продолжительность: {self.duration} ч."
