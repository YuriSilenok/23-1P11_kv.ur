""" import """
import unittest
from api import api
from fastapi.testclient import TestClient


class TestZeroABC(unittest.TestCase):
    """
        Тест для случая, когда a=0, b=0, c=0 одновременно.
        Проверяем, что API корректно обрабатывает такой запрос.
        """
    def setUp(self):
        self.client = TestClient(api)

    def test_all_zero_abc(self):
        """ Функция проверки """
        d = {'a': 0, 'b': 0, 'c': 0}
        x = 0
        response = self.client.get("/calculate", params=d)
        self.assertEqual(response.status_code, 200)
        result = response.json()

        self.assertEqual(result[0], x, 'Неверно высчитан x')

        mes1 = (
            'Это вырожденное уравнение, '
            'дискриминант высчитать невозможно'
        )
        mes2 = 'Неверное сообщение'
        self.assertEqual(len(result), 2, 'Длина кортежа не равна 2')
        self.assertEqual(result[1], mes1, mes2)
