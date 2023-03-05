import sympy as sp
from sympy.core.numbers import Rational


class Function(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        function = kwargs.get('f', None)
        self._x = sp.symbols('x')
        self._function = sp.sympify(function)
        self.clear()

    def __missing__(self, key):
        value = self._function.subs(self._x, key)

        self[key] = value
        return value

    @property
    def times_called(self):
        keys = self.keys()
        return len(keys)

    @property
    def f(self):
        return self._function


class FunctionWrapper():
    def __init__(self, *args, **kwargs):
        function = kwargs.get('function', None)
        first_dx = sp.diff(function, sp.symbols('x'))
        second_dx = sp.diff(function, sp.symbols('x'), 2)
        self._function = Function(f=function)
        self._first_dx = Function(f=first_dx)
        self._second_dx = Function(f=second_dx)

    @property
    def function(self):
        return self._function

    @property
    def first_dx(self):
        return self._first_dx

    @property
    def second_dx(self):
        return self._second_dx

    def at(self, x: float | list[float]):
        """
        Computes the value of the function at a point x.
        """
        if not self._function.f:
            raise ValueError("No function defined")
        if isinstance(x, (int, float, Rational)):
            return self._function[x]
        else:
            return [self._function[i] for i in x]

    def d1_at(self, x: float | list[float]):
        """
        Computes the first derivative of the function at a point x.
        """
        if not self._first_dx.f:
            raise ValueError("No function defined")
        if isinstance(x, (int, float, Rational)):
            return self._first_dx[x]
        else:
            return [self._first_dx[i] for i in x]

    def d2_at(self, x: float | list[float]):
        """
        Computes the second derivative of the function at a point x.
        """
        if not self._second_dx.f:
            raise ValueError("No function defined")
        if isinstance(x, (int, float, Rational)):
            return self._second_dx[x]
        else:
            return [self._second_dx[i] for i in x]
