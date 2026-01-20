from math import sqrt
from src.figure import Figure


class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

        # Проверка на возможность существования треугольника
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("Triangle with these sides cannot exist")

    @property
    def perimeter(self) -> float:
        return self.a + self.b + self.c

    @property
    def area(self) -> float:
        # Формула Герона
        s = self.perimeter / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
