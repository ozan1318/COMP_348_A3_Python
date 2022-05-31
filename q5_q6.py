class Shape:
    ID = 0

    def __init__(self):
        self.ID = 1

    def getID(self):
        return self.ID

    def print(self):
        print(self.ID, type(self).__name__ )

    def perimeter(self):
        pass

