"""Модуль тестирования квадратного уравнения"""

import unittest
from fastapi.testclient import TestClient

from main1 import app

client = TestClient(app)


class TestAPI(unittest.TestCase):
    """Класс тестирования API"""
    response = client.get("/solve?a=0&b=0&c=5")
    assert response.status_code == 400
    assert response.json() == {"detail": "Уравнение не имеет решений"}
