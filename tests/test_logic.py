"""Модуль тестирования квадратного уравнения"""

import unittest
from main import treesome


class TestKV(unittest.TestCase):
    """Тестирование квадратного уравнение"""
    def test_d_bloshe(self):
        """тест d>0"""
        a, b, c = 1, 2, -3
        d = 16
        x1, x2 = -3, 1
        result = treesome(a, b, c)
        self.assertEqual(len(result), 3, 'Длинна кортежа не равна 3')
        self.assertEqual(result[0], d, 'Неверно вычислен дискриминант')
        self.assertEqual(result[1], x1, 'Неверно вычислен x1')
        self.assertEqual(result[2], x2, 'Неверно вычислен x2')

    def test_d_equal_zero(self):
        """Тест d=0"""
        a, b, c = 2, 4, 2
        d = 0
        x = -1
        result = treesome(a, b, c)
        self.assertEqual(len(result), 2, 'Длинна кортежа не равна 2')
        self.assertEqual(result[0], d, 'Неверно вычислен дискриминант')
        self.assertEqual(result[1], x, 'Неверно вычислен x')

    def test_d_menshe(self):
        """Тест d<0"""
        a, b, c = -2, -2, -3
        d = -20
        result = treesome(a, b, c)
        self.assertEqual(len(result), 2, 'Длинна кортежа не равна 2')
        self.assertEqual(result[0], d, 'Неверно вычислен дискриминант')
        self.assertEqual(result[1],
                         "Корней нет", 
                         'Неверный результат в ответе')
