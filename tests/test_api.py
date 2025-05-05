""" Модуль тестирования квадратного уравнения API"""
import unittest
from .23-1P11_kv.ur/ import api.py
from fastapi.testclient import TestClient


class TestZeroABC(unittest.TestCase):
    """ Тестирование квадратного уравнения """
    def setUp(self):
        self.client = TestClient(api)

    def test_all_zero_abc(self):
        """ Тест a=0, b=0, c=0 """
        d = {'a': 0, 'b': 0, 'c': 0}
        x = 'Бесконечно много решений'
        response = self.client.get("/calculate", params=d)
        self.assertEqual(response.status_code, 200)
        result = response.json()

        mes1 = (
            'Это линейное уравнение, '
            'Прямая совпадает с осью Ox'
        )
        mes2 = 'Неверное сообщение'
        self.assertEqual(len(result), 2, 'Длина кортежа не равна 2')
        self.assertEqual(result[0], mes1, mes2)

        self.assertEqual(result[1], x, 'Неверно высчитан x')
