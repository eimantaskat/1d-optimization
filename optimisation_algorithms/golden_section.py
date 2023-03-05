from function_wrapper import FunctionWrapper


def golden_section(f: FunctionWrapper, l: float, r: float, eps=1e-6):
    """
    Implementation of the golden section search method for finding the minimum of
    a function f in the interval [l, r].
    """
    tau = (-1 + 5 ** 0.5) / 2

    big_l = r - l
    x1 = r - big_l * tau
    x2 = l + big_l * tau

    while big_l > eps:
        if f.at(x2) < f.at(x1):
            l = x1
            big_l = r - l
            x1 = x2
            x2 = l + big_l * tau
        else:
            r = x2
            big_l = r - l
            x2 = x1
            x1 = r - big_l * tau

    return (l + r) / 2
