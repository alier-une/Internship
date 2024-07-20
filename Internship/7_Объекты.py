# Создайте классы геометрических фигур и реализуйте логику сложения между фигурами,
# например: квадрат + квадрат = прямоугольник, прямоугольник + прямоугольник
# (при равных сторонах = квадрат, если нет, то = прямоугольник),
# и ультимативное задание (необязательно), написать логику сложения треугольников

class Figure:
    @classmethod
    def verify_addition(cls, other):
        if not isinstance(other, Figure):
            raise TypeError("You can add with each other only figures")

    @classmethod
    def verify_side(cls, *args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError("Side must be int or float")


class Square(Figure):
    def __init__(self, side):
        self.side = side
        self.verify_side(side)

    def __add__(self, other):
        self.verify_addition(other)
        if isinstance(other, Square) and self.side == other.side:
            return Rectangle.__name__
        if isinstance(other, Rectangle) and self.side in (other.width, other.height):
            return Rectangle.__name__
        else:
            raise ValueError("The sides of the figures cannot be added")


class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.verify_side(width, height)

    def __add__(self, other):
        self.verify_addition(other)
        if isinstance(other, Rectangle) and (self.height + other.height) == (self.width + other.width):
            return Square.__name__
        if isinstance(other, Rectangle) and (self.height or self.width) in (other.height, other.width):
            return Rectangle.__name__
        if isinstance(other, Square):
            Square.__add__(other, self)
            return Rectangle.__name__
        else:
            raise ValueError("The rectangle and the figure cannot be added")


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.verify_triangle(a, b, c)

    @classmethod
    def verify_triangle(cls, a, b, c):
        if a > b + c or b > a + c or c > b + a:
            raise ValueError("Invalid input")

    def __add__(self, other):
        self.verify_addition(other)
        if isinstance(other, Triangle) and (self.a, self.b, self.c) == (other.a, other.b, other.c):
            return Parallelogram.__name__
        else:
            raise ValueError("The triangle and the figure cannot be added")


class Parallelogram:
    pass


r = Rectangle(3, 7)
r1 = Rectangle(5, 1)
s = Square(3)
s1 = Square(3)
t = Triangle(3, 4, 5)
t1 = Triangle(3, 4, 5)
print(r + r1, s + s1, t + t1)
print(r1 + Rectangle(2, 1))
