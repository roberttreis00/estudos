# Property()

class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, valor):
        self._x += valor

    @x.deleter
    def x(self):
        self._x = -1


fo1 = Foo(10)
print(fo1.x)
fo1.x = 10
print(fo1.x)
del fo1.x
print(fo1.x)
