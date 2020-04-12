from inspect import getfullargspec
from math import sqrt
import math as m


class MyFunction(object):
    """Klasa z przeciazonym operatorem __call__"""
    functions = {}

    def __init__(self, name):
        """inicjalizacja z pustym slownikiem argumentow"""
        self.name = name
        self.arg_dict = {}

    def __call__(self, *args):
        """Funkcja zostaje wywolana na podstawie liczby argumentów"""
        length = len(args)
        function = self.arg_dict.get(length)

        if function is None:
            raise TypeError("Nie ma takiej funkcji")
        return function(*args)

    def add_function(self, length, function):
        """Dodanie funkcji do slownika"""
        self.arg_dict[length] = function


def overload(func):
    """Dekorator"""
    name = func.__name__
    over_func = MyFunction.functions.get(name)
    if over_func is None:
        over_func = MyFunction.functions[name] = MyFunction(name)
    over_func.add_function(len(getfullargspec(func).args), func)

    def modified(*args):
        return over_func(*args)
    return modified


@overload
def norm(x, y):
    return m.sqrt(x * x + y * y)


@overload
def norm(x, y, z):
    return abs(x) + abs(y) + abs(z)


print(f"norm(2,4) = {norm(2, 4)}")

print(f"norm(2,3,4) = {norm(2, 3, 4)}")
