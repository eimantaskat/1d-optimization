from function_wrapper import FunctionWrapper


def newton(f: FunctionWrapper, x0: float, eps=1e-6) -> tuple[float, int]:
    """
    Implementation of the Newton's method for finding the minimum of a function f
    close to the point x0.
    """
    iterations = 0
    xi = x0
    while True:
        iterations += 1
        xi1 = xi - (f.d1_at(xi) / f.d2_at(xi))
        if abs(xi1 - xi) < eps:
            break
        xi = xi1
    return float(xi), iterations
