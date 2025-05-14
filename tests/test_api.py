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
        if response.status_code == 500:
            return print("Уравнение не имеет решений")
