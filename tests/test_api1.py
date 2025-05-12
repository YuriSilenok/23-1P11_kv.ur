"""Модуль тестирования квадратного уравнения"""

import unittest
from fastapi.testclient import TestClient

from api import app

client = TestClient(app)


class TestAPI(unittest.TestCase):
    """Класс тестирования API"""
    def test_c_not_equal_zero(self):
        """Тестирование a=0, b=0, c!=0"""
        response = client.get("/solve?a=0&b=0&c=5")
        self.assertEqual(response.json() == {"detail":
                                             "Уравнение не имеет решений"})
