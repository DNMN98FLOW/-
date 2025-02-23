if __name__ == "__main__":
    # Write your solution here
    pass
class Vehicle:
    """
    Базовый класс для транспортных средств.
    """

    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Инициализация транспортного средства.

        :param brand: Бренд автомобиля
        :param model: Модель автомобиля
        :param year: Год выпуска
        """
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта для пользователя.
        """
        return f"{self.brand} {self.model} ({self.year})"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта для разработчиков.
        """
        return f"Vehicle('{self.brand}', '{self.model}', {self.year})"

    def drive(self, distance: int) -> None:
        """
        Метод для имитации движения автомобиля.

        :param distance: Пройденное расстояние в километрах
        """
        print(f"{self.brand} {self.model} проехал {distance} км.")


class Car(Vehicle):
    """
    Дочерний класс для легковых автомобилей.
    """

    def __init__(self, brand: str, model: str, year: int, seats: int) -> None:
        """
        Расширение конструктора базового класса для добавления количества мест.

        :param seats: Количество сидений в автомобиле
        """
        super().__init__(brand, model, year)
        self.seats = seats

    def __str__(self) -> str:
        """
        Перегруженный метод для добавления информации о количестве мест.
        """
        return f"{super().__str__()} - {self.seats} seats"

    def drive(self, distance: int) -> None:
        """
        Перегруженный метод drive для легковых автомобилей.
        В отличие от базового класса, добавляется сообщение о комфорте движения.
        """
        super().drive(distance)
        print(f"Поездка на {self.brand} {self.model} была комфортной!")

    def drift(self) -> None:
        """
        Метод, специфичный для легковых автомобилей (дрифтинг).
        Заднеприводные легковые автомобили могут ехать боком, поэтому
        у них добавлен режим дрифта.
        """
        print(f"{self.brand} {self.model} едет боком!")


# Пример использования
car = Car("Toyota", "Supra", 2023, 4)
print(car)  # Toyota Supra (2023) - 4 seats
car.drive(100)
car.drift()