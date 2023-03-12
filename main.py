from function_wrapper import FunctionWrapper, Function
from optimisation_algorithms import bisection, golden_section, newton
import matplotlib.pyplot as plt
import numpy as np
from typing import Callable


def get_calculated_points(function: FunctionWrapper) -> tuple[tuple[list[float]]]:
    f_values = list(function.function.keys()), list(function.function.values())
    dx1_values = list(function.first_dx.keys()), list(
        function.first_dx.values())
    dx2_values = list(function.second_dx.keys()), list(
        function.second_dx.values())
    return f_values, dx1_values, dx2_values


def draw_function(function: Callable[[float], float], l: float, r: float, color='blue', label="", num_points=1000):
    x = np.linspace(l, r, num_points)
    y = function(x)
    plt.plot(x, y, color=color, label=label)


def create_plot(function: FunctionWrapper, l: float, r: float, num_points=100, title=""):
    f_values, dx1_values, dx2_values = get_calculated_points(function)

    if f_values:
        plt.scatter(*f_values, color='red')
        draw_function(function.at, l, r, color='blue',
                      label="f(x)", num_points=num_points)

    if dx1_values[0]:
        plt.scatter(*dx1_values, color='red')
        draw_function(function.d1_at, l, r, color='green',
                      label="f'(x)", num_points=num_points)

    if dx2_values[0]:
        plt.scatter(*dx2_values, color='red')
        draw_function(function.d2_at, l, r, color='orange',
                      label="f''(x)", num_points=num_points)

    plt.xlabel("x")
    plt.ylabel("f(x)")
    ax = plt.gca()
    plt.xlim(l, r)
    plt.ylim(l, r)
    ax.set_aspect('equal', adjustable='box')
    plt.title(title)

    plt.legend()
    plt.grid()
    plt.savefig(f"./plots/{title}.png")
    plt.clf()


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
        create_plot(function, l, r, title=f"{method_name} method")
        function.function.clear()

    print("Newton's method:")
    x_min, iterations = newton(function, x0=x0, eps=eps)
    print(f"Iterations: {iterations}")
    print(f"Times f(x) was called: {function.function.times_called}")
    print(f"Times f'(x) was called: {function.first_dx.times_called}")
    print(f"Times f''(x) was called: {function.second_dx.times_called}")
    print(f"Minimum of f(x): x = {x_min}")
    print(f"f(x_min): {function.at(x_min)}")
    create_plot(function, l, r, title="Newton's method")
