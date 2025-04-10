"""Решение квадратного уравнения"""


def treesome(a, b, c):
    """Функция для вычисления корней квадратного уровнения"""
    d = b**2-4*(a*c)
    if d > 0:
        return d, (-b + d ** (0.5) / (a * 2)), (-b - d ** (0.5) / (a * 2))

    elif d == 0:
        return d, (-b / (a * 2))

    else:
        return d, "Корней нет"


if __name__ == '__main__':
    A = float(input('Введите а: '))
    B = float(input('Введите b: '))
    C = float(input('Введите c: '))
    treesome(A, B, C)
