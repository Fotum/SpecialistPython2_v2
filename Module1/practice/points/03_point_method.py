import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        """
        Расстояние между двумя точками
        """
        return math.sqrt(
            math.pow((other.x - self.x), 2) +
            math.pow((other.y - self.y), 2)
        )


# Дано две точки на координатной плоскости
point1 = Point(2, 4)
point2 = Point(5, -2)

dist = point1.distance(point2)

print("Расстояние между точками = ", dist)
