class Vehicle:
    """
    Создание и подготовка к работе объекта "Вид транспорта" (базовый класс)
    :param form: Вид транспорта
    :param model: Модель транспорта
    :param cost: Стоимость (в тыс.руб.) данной модели
    Пример:
    >>> vehicle1 = Vehicle("automobile", "BMW X6", 12000)  # инициализация экземпляра класса
    """
    def __init__(self, form: str, model: str, cost: int):
        if not isinstance(form, str):
            raise TypeError("Вид транспорта должен быть типа str")
        self.form = form
        if not isinstance(model, str):
            raise TypeError("Модель должна быть типа str")
        self.model = model
        if cost < 0:
            raise ValueError("Стоимость модели не может быть отрицательным числом")
        self.cost = cost

    def __str__(self) -> str:
        return f"Вид транспорта: {self.form}. Модель: {self.model} стоимостью {self.cost} тыс.руб."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(form={self.form!r}, model={self.model!r}, cost={self.cost!r})"

    # Метод, перегружаемый в дочернем классе
    def count_model(self) -> int:
        """
        Функция, которая считает общее количество моделей транспорта
        :return: Количество моделей
        Пример:
        >>> vehicle1 = Vehicle("automobile", "Audi R8", 35000)
        >>> vehicle1.count_model()
        """
        ...

    # Метод, который можно наследовать в дочернем классе
    def is_car(self) -> bool:
        """
        Функция, которая проверяет, является ли данный вид транспорта автомобильным
        :return: True, если транспорт автомобильный, False - если нет
        Пример:
        >>> vehicle3 = Vehicle("automobile", "Audi R8", 35000)
        >>> vehicle3.is_car()
        """
        ...


class Car(Vehicle):
    """
    Создание и подготовка к работе объекта "Машина" (дочерний класс)
    :param form: Вид транспорта (автомобильный)
    :param model: Модель автомобиля
    :param cost: Стоимость (в тыс.руб.) данной модели
    :param passenger_capacity: Количество вмещаемых пассажиров
    Пример:
    >>> car1 = Car('Автомобильный', 'Audi R8', 35000, 2) # инициализация экемпляра класса
    """

    # Расширяем конструктор базового класса, добавляя атрибут "вместимость"
    def __init__(self, form: str, model: str, cost: int, passenger_capacity: int):
        super().__init__(form, model, cost)
        if not isinstance(passenger_capacity, int):
            raise TypeError("Количество пассажиров должно быть типа int")
        if passenger_capacity <= 0:
            raise ValueError("Количество пассажиров не может быть отрицательным числом")
        self.passenger_capacity = passenger_capacity

    # Магические методы __str__ и __repr__ необходимо перегрузить, т.к. добавился атрибут "вместимость"
    def __str__(self) -> str:
        return (f"Вид транспорта: {self.form}. Модель: {self.model} стоимостью {self.cost} тыс.руб., "
                f"вместимостью {self.passenger_capacity} чел.")

    def __repr__(self) -> str:
        return (f'{self.__class__.__name__}(form={self.form!r}, model={self.model!r}, cost={self.cost!r}, '
                f'passenger_capacity={self.passenger_capacity!r})')

    def count_model(self) -> int:
        """
        Функция, которая считает общее количество моделей транспорта
        :return: Количество моделей
        Перегружаем метод, т.к. считаем количество моделей только автомобильного транспорта
        Пример:
        >>> car2 = Vehicle("automobile", "Audi R8", 35000)
        >>> car2.count_model()
        """
        ...
