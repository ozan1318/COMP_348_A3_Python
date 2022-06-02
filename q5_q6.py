import math


class Shape:
    ID = None

    def __init__(self, id_val):
        self.ID = id_val

    def getID(self):
        return self.ID

    def print(self):
        print(self.ID, type(self).__name__)

    def perimeter(self):
        pass

    def area(self):
        pass


class Circle(Shape):
    radius = None

    def __init__(self, id_val, radius):
        self.radius = radius
        self.ID = id_val

    def perimeter(self):
        return self.radius * math.pi * 2

    def area(self):
        return self.radius * math.pi * math.pi


class Ellipse(Shape):
    majax = None
    minax = None

    def __init__(self, id_val, majax, minax):
        self.ID = id_val
        self.majax = majax
        self.minax = minax

    def area(self):
        return math.pi * self.majax * self.minax

    def eccentricity(self):
        return math.sqrt((self.majax * self.majax) - (self.minax * self.minax))


class Rhombus(Shape):
    d1 = None
    d2 = None

    def __init__(self, id_val, diag_1, diag_2):
        self.ID = id_val
        self.d1 = diag_1
        self.d2 = diag_2

    def perimeter(self):
        return math.sqrt((self.d1 * self.d1) + (self.d2 * self.d2))

    def area(self):
        return (self.d1 * self.d2) / 2

    def inradius(self):
        if (self.d1 is not None) and (self.d2 is not None) and (self.d1 > 0) and (self.d2 > 0):
            return (math.pi * self.d1 * self.d1 * self.d2 * self.d2) / (4 * ((self.d1 * self.d1) + (self.d2 * self.d2)))


def read_shapes():
    file = open('q6_shapes.txt', 'r')
