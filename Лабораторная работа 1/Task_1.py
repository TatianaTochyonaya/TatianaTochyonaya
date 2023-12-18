# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Table:
    """
    Класс описывает модель стола.
    """
    def __init__(self, legs_number: int, material: str):
        """
                Создание и подготовка к работе объекта "Стол"

                :param legs_number: Количество ножек стола
                :param material: Материал, из которого сделан стол

                Пример:
                >>> table = Table(4, "пластик")  # инициализация экземпляра класса
                """
        if not isinstance(legs_number, int):
            raise TypeError("Количество ножек должно быть типа int")

        if legs_number < 0:
            raise ValueError("Ножек не может быть меньше 1")
        self.legs_number = legs_number

        self.material = material

    def table_properties(self):
        """
        Функция, которая выдаёт характеристики: материал стола и количество ножек

        :return: Значения количества ножек стола и материала стола

        Примеры:
        >>> table = Table(1, "стекло")
        >>> table.table_properties()
        """
        ...

    def is_table_wood(self) -> bool:
        """
        Функция, которая проверяет, является ли стол деревянным

        :return: Является ли стол деревянным

        Примеры:
        >>> table = Table(1, "стекло")
        >>> table.is_table_wood()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()


class Reinforcement:
    def __init__(self, estimated_area: float, min_required_area: float, rebar_diameter: int):
        """
        Создание и подготовка к работе объекта "Армирование"

        :param estimated_area: Расчётная площадь арматуры
        :param min_required_area: Минимальная требуемая площадь арматуры
        :param rebar_diameter: Диаметр арматуры

        Примеры:
        >>> Rebar = Reinforcement(40, 10, 12)  # инициализация экземпляра класса
        """
        if estimated_area < 0:
            raise ValueError("Площадь арматуры не может быть отрицательным числом")
        self.estimated_area = estimated_area

        if min_required_area < 0:
            raise ValueError("Площадь арматуры не может быть отрицательным числом")
        self.min_required_area = min_required_area

        if not isinstance(rebar_diameter, int):
            raise TypeError("Диаметр арматуры должен быть типа int")
        if rebar_diameter < 6:
            raise ValueError("Диаметр арматуры не может быть меньше 6")
        self.rebar_diameter = rebar_diameter

    def is_reinforcement_provided(self) -> bool:
        """
        Функция, которая проверяет, обеспечена ли минимальная требуемая площадь арматуры

        :return: Обеспечена ли минимальная требуемая площадь арматуры

        Примеры:
        >>> rebar = Reinforcement(80, 10, 6)
        >>> rebar.is_reinforcement_provided()
        """
        ...

    def reinforcement_encrease(self, additional_reinforcement: float) -> None:
        """
        Функция, которая увеличивает расчетную площадь армирования на величину дополнительной арматуры
        :param additional_reinforcement: Площадь дополнительной арматуры

        :return: Площадь расчетной арматуры с учетом дополнительной

        Примеры:
        >>> reinforcement = Reinforcement(100, 50, 10)
        >>> reinforcement.reinforcement_encrease(10)
        """
        if not isinstance(additional_reinforcement, (int, float)):
            raise TypeError("Дополнительная арматура должна быть типа int или float")
        if additional_reinforcement < 0:
            raise ValueError("Дополнительная арматура не может быть отрицательным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()


class Steps:
    """
    Класс описывает количество шагов.
    """
    def __init__(self, step_count: int, desired_steps_number: int):
        """
                Создание и подготовка к работе объекта "Шаги"

                :param step_count: Количество реально пройденных шагов
                :param desired_steps_number: Желамое количество шагов в день

                Пример:
                >>> steps = Steps(5500, 10000)  # инициализация экземпляра класса
                """
        if not isinstance(step_count, int):
            raise TypeError("Количество шагов должно быть типа int")
        self.step_count = step_count

        if not isinstance(desired_steps_number, int):
            raise TypeError("Желаемое количество шагов должно быть типа int")
        self.desired_steps_number = desired_steps_number

    def steps_goal_completed(self) -> bool:
        """
       Функция проверяет, не меньше ли число реально пройденных шагов по сравнению с желаемым количеством

        :return: Сделано ли желамое количество шагов

        Примеры:
        >>> steps = Steps(9000, 10000)
        >>> steps.steps_goal_completed()
        """
        ...

    def add_steps(self, new_steps: int) -> None:
        """
        Добавление новых шагов к изначальному количеству.
        :param new_steps: Количество новых шагов

        Примеры:
        >>> my_steps = Steps(5000, 120000)
        >>> my_steps.add_steps(2600)
        """
        if not isinstance(new_steps, int):
            raise TypeError("Количество новых шагов должно быть типа int")
        ...


if __name__ == "__main__":
    doctest.testmod()
