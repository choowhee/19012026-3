from abc import ABC, abstractmethod


class Figure(ABC):
    @property
    @abstractmethod
    def area(self) -> float:
        """Возвращает площадь фигуры"""
        pass

    @property
    @abstractmethod
    def perimeter(self) -> float:
        """Возвращает периметр фигуры"""
        pass

    def add_area(self, other: "Figure") -> float:
        """
        Возвращает сумму площадей текущей фигуры и другой фигуры.
        Если другой объект не является Figure, выбрасывает ValueError.
        """
        if not isinstance(other, Figure):
            raise ValueError("Argument must be a Figure instance")
        return self.area + other.area
