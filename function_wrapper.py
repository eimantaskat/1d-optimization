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
        self._derivatives = {}
        self._function = Function(f=function)

    @property
    def function(self):
        return self._function
    
    @property
    def derivatives(self):
        return self._derivatives

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

    def dx_at(self, x: float | list[float], order: int = 1):
        """
        Computes the value of the n-th derivative of the function at a point x.
        """
        if not self._derivatives.get(order):
            self._derivatives[order] = Function(
                f=sp.diff(self._function.f, sp.symbols('x'), order))
        if isinstance(x, (int, float, Rational)):
            return self._derivatives[order][x]
        else:
            return [self._derivatives[order][i] for i in x]
