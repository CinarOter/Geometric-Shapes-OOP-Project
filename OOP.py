from math import pi

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {"filled" if self.is_filled else "not filled"}.")


class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"It is a circle with an area of {(self.radius ** 2) * pi:.2f}cm²")


class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

    def describe(self):
        super().describe()
        print(f"It is a square with an area of {self.width ** 2}cm²")


class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"It is a triangle with an area of {(self.height * self.width)/2}cm²")


if __name__ == "__main__":

    circle = Circle("red", True, 5)
    square = Square("blue", False, 6)
    triangle = Triangle("yellow", True, 7, 8)

    circle.describe()
    print('-' * 25)
    square.describe()
    print('-' * 25)
    triangle.describe()
