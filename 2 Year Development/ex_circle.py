from math import pi
from functools import cached_property


class Circle:

    # '*' costringe tutto quello che c'è nel metodo ad essere passato per nome
    # def __init__(self, *, radius=-1, diameter=-1):
    #     if radius <= 0:
    #         raise ValueError("Radius must be greater than 0")
    #     self.__radius = radius
    # circle = Circle(radius=5)
    # circle = Circle(diameter=5)

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be greater than 0")
        self.__radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    def __repr__(self):
        return f"(Circle{self.radius}, {self.diameter})"

    def __str__(self):
        return f"Your circle has {self.radius} of radius, {self.diameter} of diameter and {self.area} of area."

    def _add__(self, other):
        if other is Circle:
            circleSum = Circle(self.radius + other.radius)
            return circleSum
        else:
            return 0

    def __gt__(self, other):
        return self.radius > other.radius

    def eq(self, other):
        return self.radius == other.radius

    @property
    def radius(self):
        if self.__radius:
            return self.__radius

    @radius.setter
    def radius(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be greater than 0")
        self.__radius = radius

    @cached_property
    def diameter(self):
        return self.radius * 2

    @cached_property
    def area(self):
        return pi*pow(self.radius, 2)


my_circle = Circle(5)
my_circle2 = Circle(10)
super_circle = my_circle + my_circle2
print(my_circle)
print(my_circle2)
print(super_circle)
print(my_circle.diameter)
print(my_circle.radius)
print(my_circle.area)
print(my_circle2.diameter)
print(my_circle2.radius)
print(my_circle2.area)
print(super_circle.diameter)
print(super_circle.radius)
print(super_circle.area)
print(my_circle == my_circle2)
print(my_circle < my_circle2)

list_of_circles = []
list_of_circles.append(my_circle)
list_of_circles.append(super_circle)
list_of_circles.append(my_circle2)
list_of_circles.sort()
print(list_of_circles)

circle = Circle(5)
circle_from_diameter = Circle.from_diameter(10)
