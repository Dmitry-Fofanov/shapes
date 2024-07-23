import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.sides = sorted((side1, side2, side3))
        # Сохраняем стороны в порядке возрастания
        # Для избежания повторных сортировок

    def get_area(self):
        half_sum = sum(self.sides) / 2
        return math.sqrt(
            half_sum
            * (half_sum - self.sides[0])
            * (half_sum - self.sides[1])
            * (half_sum - self.sides[2])
        )

    def is_right_triangle(self):
        return math.isclose(
            self.sides[0] ** 2 + self.sides[1] ** 2,
            self.sides[2] ** 2,
        )
