"""Решение квадратного уравнения"""


def treesome(a, b, c):
    """Функция для вычисления корней квадратного уровнения"""
    d = b**2-4*(a*c)
    if d > 0:
        print('x1= ', (-b + d ** (0.5) / (a * 2)))
        print('x2= ', (-b - d ** (0.5) / (a * 2)))

    if d == 0:
        print('x= ', (-b / (a * 2)))

    if d < 0:
        print("Корней нет")


if __name__ == '__main__':
    a = float(input('Введите а: '))
    b = float(input('Введите b: '))
    c = float(input('Введите c: '))
    treesome(a, b, c)
