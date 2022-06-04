import math


class Shape:
    ID = None
    valid = None

    def __init__(self, id_val, valid=True):
        self.ID = id_val
        self.valid = valid

    def print(self):
        print(self.ID, ": ", type(self).__name__, ", ", sep="", end="")
        if type(self).__name__ == 'Shape':
            print("perimeter: undefined, area: undefined")
        elif type(self).__name__ == 'Circle':
            if self.area() is not None and self.perimeter() is not None:
                print("perimeter: ", round(self.perimeter(), 5), ", area: ", round(self.area(), 5), sep="")
            elif self.area() is not None:
                print("perimeter: ", self.perimeter(), ", area: ", round(self.area(), 5), sep="")
            elif self.perimeter() is not None:
                print("perimeter: ", round(self.perimeter(), 5), ", area: ", self.area(), sep="")
            else:
                print("perimeter: ", self.perimeter(), ", area: ", self.area(), sep="")
            if not self.valid:
                print("Error: Invalid Circle")
        elif type(self).__name__ == 'Ellipse':
            if self.area() is not None and self.perimeter() is not None:
                print("perimeter: ", round(self.perimeter(), 5), ", area: ", round(self.area(), 5), sep="")
            elif self.area() is not None:
                print("perimeter: ", self.perimeter(), ", area: ", round(self.area(), 5), sep="")
            elif self.perimeter() is not None:
                print("perimeter: ", round(self.perimeter(), 5), ", area: ", self.area(), sep="")
            else:
                print("perimeter: ", self.perimeter(), ", area: ", self.area(), sep="")
            if self.valid:
                print("linear eccentricity:", round(self.eccentricity(), 5))
            else:
                print("Error: Invalid Ellipse")
        elif type(self).__name__ == 'Rhombus':
            if self.area() is not None and self.perimeter() is not None:
                print("perimeter: ", round(self.perimeter(), 5), ", area: ", round(self.area(), 5), sep="")
            elif self.area() is not None:
                print("perimeter: ", self.perimeter(), ", area: ", round(self.area(), 5), sep="")
            elif self.perimeter() is not None:
                print("perimeter: ", round(self.perimeter(), 5), ", area: ", self.area(), sep="")
            else:
                print("perimeter: ", self.perimeter(), ", area: ", self.area(), sep="")
            if self.valid:
                if self.inradius() is not None:
                    print("in-radius:", round(self.inradius(), 5))
                else:
                    print("in-radius:", self.inradius())
            else:
                print("Error: Invalid Rhombus")

    def perimeter(self):
        pass

    def area(self):
        pass


class Circle(Shape):
    radius = None

    def __init__(self, id_val, radius, valid=True):
        self.radius = radius
        self.ID = id_val
        self.valid = valid

    def perimeter(self):
        if self.valid:
            return self.radius * math.pi * 2

    def area(self):
        if self.valid:
            return self.radius * math.pi * math.pi


class Ellipse(Shape):
    majax = None
    minax = None

    def __init__(self, id_val, ax1, ax2, valid=True):
        self.ID = id_val
        if ax1 >= ax2:
            self.majax = ax1
            self.minax = ax2
        else:
            self.majax = ax2
            self.minax = ax1
        self.valid = valid

    def area(self):
        if self.valid:
            return math.pi * self.majax * self.minax

    def eccentricity(self):
        if self.valid:
            return math.sqrt((self.majax * self.majax) - (self.minax * self.minax))


class Rhombus(Shape):
    d1 = None
    d2 = None

    def __init__(self, id_val, diag_1, diag_2, valid=True):
        self.ID = id_val
        self.d1 = diag_1
        self.d2 = diag_2
        self.valid = valid

    def perimeter(self):
        if self.valid:
            return math.sqrt((self.d1 * self.d1) + (self.d2 * self.d2))

    def area(self):
        if self.valid:
            return (self.d1 * self.d2) / 2

    def inradius(self):
        if self.valid and (self.d1 is not None) and (self.d2 is not None) and (self.d1 > 0) and (self.d2 > 0):
            return (math.pi * self.d1 * self.d1 * self.d2 * self.d2) / (4 * ((self.d1 * self.d1) + (self.d2 * self.d2)))


def read_shapes(id_val, filename, shape_list):
    with open(filename, 'r') as file:
        lines = file.readlines()

    for x in lines:
        if x == "shape\n":
            shape_list.append(Shape(id_val))
        else:
            y = x.split(" ")
            if y[0] == "circle":
                if len(y) == 2:
                    if int(y[1]) > 0:
                        shape_list.append(Circle(id_val, int(y[1])))
                    else:
                        shape_list.append(Circle(id_val, y[1], False))
                else:
                    shape_list.append(Circle(id_val, None, False))
            elif y[0] == "ellipse":
                if len(y) == 3:
                    if int(y[1]) >= 0 and int(y[2]) >= 0:
                        shape_list.append(Ellipse(id_val, int(y[1]), int(y[2])))
                    else:
                        shape_list.append(Ellipse(id_val, int(y[1]), int(y[2]), False))
                else:
                    shape_list.append(Ellipse(id_val, None, None))
            elif y[0] == "rhombus":
                if len(y) == 3:
                    if int(y[1]) >= 0 and int(y[2]) >= 0:
                        shape_list.append(Rhombus(id_val, int(y[1]), int(y[2])))
                    else:
                        shape_list.append(Rhombus(id_val, int(y[1]), int(y[2]), False))
                else:
                    shape_list.append(Rhombus(id_val, None, None))
        id_val += 1


def q6_main():
    id_val = 1
    filename = 'q6_shapes.txt'
    shape_list = []

    read_shapes(id_val, filename, shape_list)

    for x in shape_list:
        x.print()


q6_main()
