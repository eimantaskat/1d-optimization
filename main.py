from function_wrapper import FunctionWrapper
from optimisation_algorithms import bisection, golden_section, newton
import matplotlib.pyplot as plt
import numpy as np
from typing import Callable


def get_calculated_points(function: FunctionWrapper) -> tuple[tuple[list[float]]]:
    f_values = list(function.function.keys()), list(function.function.values())
    dx1_values = ([], [])
    dx2_values = ([], [])
    if function.derivatives.get(1):
        dx1_values = list(function.derivatives.get(1).keys()), list(
            function.derivatives.get(1).values())
    if function.derivatives.get(2):
        dx2_values = list(function.derivatives.get(2).keys()), list(
            function.derivatives.get(2).values())
    return f_values, dx1_values, dx2_values


def draw_function(function: Callable[[float], float], l: float, r: float, color='blue', label="", num_points=1000, dx_order=0):
    x = np.linspace(l, r, num_points)
    if dx_order == 0:
        y = function(x)
    else:
        y = function(x, order=dx_order)
    plt.plot(x, y, color=color, label=label)


def create_plot(function: FunctionWrapper, l: float, r: float, num_points=100, title=""):
    f_values, dx1_values, dx2_values = get_calculated_points(function)
    if f_values:
        plt.scatter(*f_values, facecolors='none', edgecolors='r', s=10)
        draw_function(function.at, l, r, color='blue',
                      label="f(x)", num_points=num_points)

    if dx1_values[0]:
        plt.scatter(*dx1_values, facecolors='none', edgecolors='r', s=10)
        draw_function(function.dx_at, l, r, color='green',
                      label="f'(x)", num_points=num_points, dx_order=1)

    if dx2_values[0]:
        plt.scatter(*dx2_values, facecolors='none', edgecolors='r', s=10)
        draw_function(function.dx_at, l, r, color='orange',
                      label="f''(x)", num_points=num_points, dx_order=2)

    plt.xlabel("x")
    plt.ylabel("f(x)")
    ax = plt.gca()
    plt.xlim(-10, 10)
    plt.ylim(-2, 18)
    ax.set_aspect('equal', adjustable='box')
    plt.title(title)

    plt.legend()
    plt.grid()
    plt.savefig(f"./plots/{title}.png")
    plt.show()


if __name__ == '__main__':
    function = FunctionWrapper(function="((x**2 - 5)**2)/2-1")
    l = 0
    r = 10
    x0 = 5
    eps = 1e-4

    for method in [bisection, golden_section]:
        method_name = method.__name__.capitalize().replace("_", " ")
        print(f"{method_name} method:")
        x_min, iterations = method(function, l=l, r=r, eps=eps)
        print(f"Iterations: {iterations}")
        print(f"Times f(x) was called: {function.function.times_called}")
        print(f"Minimum of f(x): x = {x_min}")
        print(f"f(x_min): {function.at(x_min)}\n")
        create_plot(function, -5, 5, title=f"{method_name} method")
        function.function.clear()

    print("Newton's method:")
    x_min, iterations = newton(function, x0=x0, eps=eps)
    print(f"Iterations: {iterations}")
    print(f"Times f(x) was called: {function.function.times_called}")
    print(f"Times f'(x) was called: {function.derivatives.get(1).times_called}")
    print(f"Times f''(x) was called: {function.derivatives.get(2).times_called}")
    print(f"Minimum of f(x): x = {x_min}")
    print(f"f(x_min): {function.at(x_min)}")
    create_plot(function, -5, 5, title="Newton's method")
