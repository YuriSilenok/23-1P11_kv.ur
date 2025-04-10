"""Решение квадратного уровнение """
a = float(input('Введите а'))
b = float(input('Введите b'))
c = float(input('Введите c'))
d = b**2-4*(a*c)
if d > 0:
    print('x1= ', (-b + d ** (0.5) / (a * 2)))
