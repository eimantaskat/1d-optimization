from function_wrapper import FunctionWrapper


def bisection(f: FunctionWrapper, l: float, r: float, eps=1e-6):
    """
    Implementation of the bisection method for finding the minimum of a function f
    in the interval [l, r].
    """
    xm = (l + r) / 2
    big_l = r - l

    while big_l > eps:
        x1 = l + big_l / 4
        x2 = r - big_l / 4
        if f.at(x1) < f.at(xm):
            r = xm
            xm = x1
        elif f.at(x2) < f.at(xm):
            l = xm
            xm = x2
        else:
            l = x1
            r = x2
        big_l = r - l

    return xm
