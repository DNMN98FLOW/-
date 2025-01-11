# TODO Написать 3 класса с документацией и аннотацией типов
class Car:
    """
    Атрибуты:
        make (str): Марка автомобиля.
        model (str): Модель автомобиля.
        year (int): Год выпуска автомобиля.
    """

    def __init__(self, make: str, model: str, year: int):
        if year < 1886:  # Первый автомобиль изобретен в 1886 году.
            raise ValueError("Год выпуска автомобиля должен быть не ранее 1886 года.")
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self) -> str:
        """
        Запускает двигатель автомобиля.
        Возвращает:
            str: Сообщение о запуске двигателя.
        Пример:
        >>> car = Car("Toyota", "Camry", 2020)
        >>> car.start_engine()
        'Двигатель автомобиля Toyota Camry запущен.'
        """
        return f"Двигатель автомобиля {self.make} {self.model} запущен."

    def stop_engine(self) -> str:
        """
        Останавливает двигатель автомобиля.
        Возвращает:
            str: Сообщение об остановке двигателя.
        Пример:
        >>> car = Car("Toyota", "Camry", 2020)
        >>> car.stop_engine()
        'Двигатель автомобиля Toyota Camry остановлен.'
        """
        return f"Двигатель автомобиля {self.make} {self.model} остановлен."

class Book:
    """
    Класс, представляющий книгу.

    Атрибуты:
        title (str): Название книги.
        author (str): Автор книги.
        pages (int): Количество страниц.
    """

    def __init__(self, title: str, author: str, pages: int):
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")
        self.title = title
        self.author = author
        self.pages = pages

    def read(self, pages_read: int) -> str:
        """
        Читает указанное количество страниц.

        Args:
            pages_read (int): Количество прочитанных страниц.

        Возвращает:
            str: Сообщение о количестве прочитанных страниц.

        Пример:
        >>> book = Book("Война и мир", "Лев Толстой", 1225)
        >>> book.read(100)
        'Вы прочитали 100 страниц из книги "Война и мир".'
        """
        if pages_read <= 0:
            raise ValueError("Количество прочитанных страниц должно быть положительным числом.")
        if pages_read > self.pages:
            raise ValueError("Количество прочитанных страниц не может превышать общее количество страниц.")
        return f'Вы прочитали {pages_read} страниц из книги "{self.title}".'

    def __str__(self) -> str:
        """
        Возвращает строковое представление книги.

        Пример:
        >>> book = Book("Война и мир", "Лев Толстой", 1225)
        >>> str(book)
        'Книга "Война и мир" автора Лев Толстой на 1225 страниц.'
        """
        return f'Книга "{self.title}" автора {self.author} на {self.pages} страниц.'


class Laptop:
    """
    Атрибуты:
        brand (str): Бренд ноутбука.
        model (str): Модель ноутбука.
        battery_level (int): Уровень заряда батареи (в процентах).
    """

    def __init__(self, brand: str, model: str, battery_level: int):
        if not (0 <= battery_level <= 100):
            raise ValueError("Уровень заряда батареи должен быть в диапазоне от 0 до 100.")
        self.brand = brand
        self.model = model
        self.battery_level = battery_level

    def charge(self, amount: int) -> str:
        """
        Заряжает ноутбук на указанное количество процентов.

        Args:
            amount (int): Количество процентов для зарядки.

        Возвращает:
            str: Сообщение о текущем уровне заряда.

        Пример:
        >>> laptop = Laptop("Apple", "MacBook Air", 50)
        >>> laptop.charge(30)
        'Уровень заряда: 80%.'
        """
        if amount <= 0:
            raise ValueError("Количество процентов для зарядки должно быть положительным.")
        self.battery_level = min(100, self.battery_level + amount)
        return f"Уровень заряда: {self.battery_level}%."

    def use(self, hours: int) -> str:
        """
        Таймер сна через определенное колличество часов
        Args:
            hours (int): Количество часов использования.
        Возвращает:
            str: Сообщение о текущем уровне заряда.

        Пример:
        >>> laptop = Laptop("Apple", "MacBook Air", 50)
        >>> laptop.use(2)
        'Оставшийся заряд: 30%.'
        """
        if hours <= 0:
            raise ValueError("Количество часов должно быть положительным.")
        self.battery_level = max(0, self.battery_level - hours * 10)  # Допустим, расход 10% в час.
        return f"Оставшийся заряд: {self.battery_level}%."


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
