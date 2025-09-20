import math
import numpy as np
import matplotlib.pyplot as plt

extremum = []


# noinspection PyBroadException
def f(x):
    return math.sin(x) ** 2 - 2 * math.tan(x)  # math.asin(x)**2


def find_x(epsilon: int, section: list[int | float]):
    _a = section[0]
    _b = section[1]
    _x = []
    while _a <= _b:
        _x.append(_a)
        _a += epsilon
    return _x

def golden_section(user_func, _a, _b, eps):
    l = _b - _a
    while l>=eps:
        x1 = _a + 0.381966 * l
        x2 = _a + 0.618034 * l
        y1 = user_func(x1)
        y2 = user_func(x2)
        if y1 < y2:
            _b = x2
        else:
            _a = x1
        l = _b - _a
    return _a

a, b, eps = 0, 2, 0.001
result = round(golden_section(f, a, b, eps), 2)
result_y = f(result)
x = find_x(eps, [a, b])
y = [f(i) for i in x]

plt.plot(x, y, 'b-', label='y(x)')
plt.plot( result, result_y, 'ro', label=f'Minimum at x={result:.3f}')
plt.title('Function and Golden Section Minimum')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()

