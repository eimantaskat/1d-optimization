from function_wrapper import FunctionWrapper


def newton(f: FunctionWrapper, x0: float, eps=1e-6):
    """
    Implementation of the Newton's method for finding the minimum of a function f
    close to the point x0.
    """
    xi = x0
    while True:
        xi1 = xi - (f.d1_at(xi) / f.d2_at(xi))
        if abs(xi1 - xi) < eps:
            break
        xi = xi1
    return xi
