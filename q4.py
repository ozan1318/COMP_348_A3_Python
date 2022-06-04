class multiset:
    mset = []

    def __init__(self, mset_lst):
        self.mset = list(mset_lst)
        self.mset.sort()

    def __add__(self, other):
        self.mset.append(other)
        self.mset.sort()

    def __truediv__(self, other):
        while self.mset.count(other) > 0:
            self.mset.remove(other)
        self.mset.sort()

    def __sub__(self, other):
        if type(other) is multiset:
            for x in other.mset:
                self.mset.remove(x)
        elif type(other) is list:
            for x in other:
                self.mset.remove(x)
        elif type(other) is tuple or set:
            other = list(other)
            for x in other:
                self.mset.remove(x)
        self.mset.sort()

    def union(self, other):
        if type(other) is multiset:
            for x in other.mset:
                self.mset.append(x)
        elif type(other) is list:
            for x in other:
                self.mset.append(x)
        elif type(other) is tuple or set:
            other = list(other)
            for x in other:
                self.mset.append(x)
        self.mset.sort()

    def intersect(self, other):
        acc = []
        t = []
        if type(other) is multiset:
            t = other.mset
        elif type(other) is tuple or set:
            t = list(other)
        else:
            t = other
        for x in self.mset:
            if t.count(x) > 0:
                acc.append(x)
                t.remove(x)
                self.mset.remove(x)
        acc.sort()
        print(*acc)

    def m(self, element):
        print(self.mset.count(element))